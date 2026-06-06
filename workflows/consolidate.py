#!/usr/bin/env python3
"""Deterministic consolidation of QG fragment JSONs into unified core-data registries.

Zero-LLM merging: dedup references/formulas/problems, build concept graph + connection
matrix + digest. Judgment calls (near-duplicate concepts) are only FLAGGED into
core-data/_review/ for an agent to decide; decisions are applied with --apply-merges.

Usage:
  python3 consolidate.py                 # build all registries from fragments
  python3 consolidate.py --apply-merges  # apply _review/merge-decisions.json to concept graph
"""
import json, glob, re, sys, os, difflib
from collections import defaultdict

ROOT = '/Users/pazny/projects/theoryOfEverything'
CD = ROOT + '/core-data'
REVIEW = CD + '/_review'
RANK = {'barely': 0, 'partially': 1, 'well': 2}


def jdump(path, obj):
    with open(path, 'w') as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)
        f.write('\n')


def norm_arxiv(a):
    if not a:
        return None
    a = str(a).lower().replace('arxiv:', '').strip()
    a = re.sub(r'v\d+$', '', a)
    return a or None


def norm_title(t):
    return re.sub(r'[^a-z0-9]', '', (t or '').lower())


def load_fragments():
    frags = {}
    for f in sorted(glob.glob(CD + '/fragments/*.json')):
        d = json.load(open(f))
        frags[d['slug']] = d
    return frags


def merge_references(frags):
    merged = {}
    for slug, d in frags.items():
        for r in d.get('references', []):
            key = norm_arxiv(r.get('arxiv')) or (r.get('doi') or '').lower() or norm_title(r.get('title'))
            if not key:
                continue
            if key in merged:
                m = merged[key]
                m['pillars'] = sorted(set(m['pillars']) | {slug})
                if len(r.get('significance') or '') > len(m.get('significance') or ''):
                    m['significance'] = r['significance']
                for fld in ('arxiv', 'doi', 'url', 'authors', 'title', 'year'):
                    if not m.get(fld) and r.get(fld):
                        m[fld] = r[fld]
            else:
                merged[key] = {k: r.get(k) for k in ('id', 'authors', 'title', 'year', 'arxiv', 'doi', 'url', 'significance')}
                merged[key]['pillars'] = [slug]
    refs = sorted(merged.values(), key=lambda r: (r.get('year') or 0, r.get('title') or ''))
    return refs


def bibtex(refs):
    seen, out = set(), []
    for r in refs:
        first = re.split(r'[,;]| and ', r.get('authors') or 'unknown')[0].strip()
        surname = re.sub(r'[^a-z]', '', first.split()[-1].lower()) if first else 'unknown'
        words = re.findall(r'[a-z]{4,}', (r.get('title') or '').lower())
        word = next((w for w in words if w not in ('with', 'from', 'theory', 'towards', 'toward')), 'work')
        base = '%s%s%s' % (surname or 'unknown', r.get('year') or '', word)
        key, i = base, 98
        while key in seen:
            key = base + chr(i)
            i += 1
        seen.add(key)
        kind = 'article' if (r.get('arxiv') or r.get('doi')) else 'misc'
        fields = ['  author = {%s}' % (r.get('authors') or ''),
                  '  title = {%s}' % (r.get('title') or ''),
                  '  year = {%s}' % (r.get('year') or '')]
        if r.get('arxiv'):
            fields += ['  eprint = {%s}' % r['arxiv'], '  archivePrefix = {arXiv}']
        if r.get('doi'):
            fields.append('  doi = {%s}' % r['doi'])
        if r.get('url') and not r.get('arxiv'):
            fields.append('  url = {%s}' % r['url'])
        out.append('@%s{%s,\n%s\n}' % (kind, key, ',\n'.join(fields)))
    return '\n\n'.join(out) + '\n'


def merge_formulas(frags):
    merged = {}
    for slug, d in frags.items():
        for f in d.get('formulas', []):
            key = re.sub(r'\s+', '', f.get('latex') or '') or (slug + ':' + (f.get('id') or ''))
            if key in merged:
                m = merged[key]
                m['pillars'] = sorted(set(m['pillars']) | {slug})
                if len(f.get('meaning') or '') > len(m.get('meaning') or ''):
                    m['meaning'] = f['meaning']
            else:
                merged[key] = {k: f.get(k) for k in ('id', 'name', 'latex', 'meaning', 'source')}
                merged[key]['pillars'] = [slug]
    return list(merged.values())


def merge_problems(frags):
    by_id = {}
    for slug, d in frags.items():
        for p in d.get('openProblems', []):
            pid = p.get('id') or norm_title(p.get('statement'))[:40]
            if pid in by_id:
                m = by_id[pid]
                m['pillars'] = sorted(set(m['pillars']) | {slug})
                if len(p.get('statement') or '') > len(m.get('statement') or ''):
                    m['statement'] = p['statement']
            else:
                by_id[pid] = {k: p.get(k) for k in ('id', 'statement', 'whyHard', 'attempts')}
                by_id[pid]['id'] = pid
                by_id[pid]['pillars'] = [slug]
    cands = []
    ids = list(by_id)
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            r = difflib.SequenceMatcher(None, ids[i], ids[j]).ratio()
            if r >= 0.72:
                cands.append({'a': ids[i], 'b': ids[j], 'ratio': round(r, 2)})
    probs = sorted(by_id.values(), key=lambda p: -len(p['pillars']))
    return probs, cands


def build_graph(frags):
    nodes, edges = {}, {}
    for slug, d in frags.items():
        nodes[slug] = {'id': slug, 'name': d.get('name', slug), 'type': 'pillar',
                       'definition': '', 'aliases': [], 'pillars': [slug]}

    def add_edge(f, t, typ, desc, explored, src):
        if not f or not t or f == t:
            return
        k = (f, t, typ)
        if k in edges:
            e = edges[k]
            e['sourcePillars'] = sorted(set(e['sourcePillars']) | {src})
            if desc and len(desc) > len(e.get('description') or ''):
                e['description'] = desc
            if explored:
                cur = e.get('explored')
                if cur is None or RANK.get(explored, 1) < RANK.get(cur, 1):
                    e['explored'] = explored
        else:
            edges[k] = {'from': f, 'to': t, 'type': typ, 'description': desc or '',
                        'explored': explored, 'sourcePillars': [src]}

    for slug, d in frags.items():
        for c in d.get('concepts', []):
            cid = c.get('id')
            if not cid:
                continue
            if cid in nodes:
                n = nodes[cid]
                n['pillars'] = sorted(set(n['pillars']) | {slug})
                if len(c.get('definition') or '') > len(n.get('definition') or ''):
                    n['definition'] = c['definition']
            else:
                nodes[cid] = {'id': cid, 'name': c.get('name', cid), 'type': 'concept',
                              'definition': c.get('definition', ''), 'aliases': [], 'pillars': [slug]}
            for rt in c.get('relatedTo') or []:
                add_edge(cid, rt, 'related-concept', '', None, slug)
        for cn in d.get('connections', []):
            add_edge(cn.get('from', slug), cn.get('to', ''), cn.get('type', 'shared-structure'),
                     cn.get('description', ''), cn.get('explored'), slug)
    for (f, t, _), e in list(edges.items()):
        for x in (f, t):
            if x not in nodes:
                nodes[x] = {'id': x, 'name': x, 'type': 'stub', 'definition': '',
                            'aliases': [], 'pillars': sorted(e['sourcePillars'])}
    return nodes, edges


def concept_merge_candidates(nodes):
    cands = []
    ids = [i for i, n in nodes.items() if n['type'] != 'pillar']
    names = {i: nodes[i]['name'].lower() for i in ids}
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            a, b = ids[i], ids[j]
            r = difflib.SequenceMatcher(None, names[a], names[b]).ratio()
            sub = (a in b or b in a) and min(len(a), len(b)) >= 8
            if r >= 0.82 or sub:
                cands.append({'a': a, 'b': b, 'nameA': nodes[a]['name'], 'nameB': nodes[b]['name'],
                              'defA': (nodes[a]['definition'] or '')[:220], 'defB': (nodes[b]['definition'] or '')[:220],
                              'pillarsA': nodes[a]['pillars'], 'pillarsB': nodes[b]['pillars'],
                              'nameSimilarity': round(r, 2)})
    return cands


def build_connections(frags, slugs):
    conns = {}
    for slug, d in frags.items():
        for cn in d.get('connections', []):
            k = (cn.get('from', slug), cn.get('to', ''), cn.get('type', ''))
            if not k[0] or not k[1]:
                continue
            if k in conns:
                e = conns[k]
                e['sourcePillars'] = sorted(set(e['sourcePillars']) | {slug})
                ex = cn.get('explored')
                if ex and e.get('explored') and ex != e['explored']:
                    e['description'] += ' [rating disagreement: %s says %s]' % (slug, ex)
                    if RANK.get(ex, 1) < RANK.get(e['explored'], 1):
                        e['explored'] = ex
                elif len(cn.get('description') or '') > len(e.get('description') or ''):
                    e['description'] = cn['description']
            else:
                conns[k] = {'from': k[0], 'to': k[1], 'type': k[2],
                            'description': cn.get('description', ''),
                            'explored': cn.get('explored'), 'sourcePillars': [slug]}
    cl = list(conns.values())
    matrix = {a: {b: 'none' for b in slugs if b != a} for a in slugs}
    for e in cl:
        a, b = e['from'], e['to']
        if a in matrix and b in matrix and a != b:
            cur = matrix[a][b]
            new = e.get('explored') or 'partially'
            if cur == 'none' or RANK.get(new, 1) > RANK.get(cur, -1):
                matrix[a][b] = new
    return cl, matrix


def write_digest(nodes, edges, refs, formulas, probs, conns):
    deg = defaultdict(int)
    for e in (edges.values() if isinstance(edges, dict) else edges):
        deg[e['from']] += 1
        deg[e['to']] += 1
    hubs = sorted(((d, i) for i, d in deg.items()
                   if isinstance(nodes, dict) and nodes.get(i, {}).get('type') == 'concept'), reverse=True)[:15]
    barely = [c for c in conns if c.get('explored') == 'barely']
    lines = ['# Core-data digest (auto-generated by consolidate.py — cheap entry point for agents)',
             '',
             'Totals: %d graph nodes, %d edges, %d unique references, %d formulas, %d open problems, %d cross-connections (%d rated barely explored).' % (
                 len(nodes), len(edges), len(refs), len(formulas), len(probs), len(conns), len(barely)),
             '', '## Top concept hubs (by graph degree)']
    lines += ['- %s (degree %d, pillars: %s)' % (i, d, ', '.join(nodes[i]['pillars'])) for d, i in hubs]
    lines += ['', '## Barely explored connections — THE HUNTING GROUND (full list)']
    lines += ['- %s -> %s [%s] %s' % (c['from'], c['to'], c['type'], (c['description'] or '')[:240]) for c in barely]
    lines += ['', '## Most-shared open problems']
    lines += ['- %s (pillars: %s)' % (p['id'], ', '.join(p['pillars'])) for p in probs[:12]]
    with open(CD + '/_digest.md', 'w') as f:
        f.write('\n'.join(lines) + '\n')
    return len(barely), [i for _, i in hubs]


def main():
    os.makedirs(REVIEW, exist_ok=True)
    frags = load_fragments()
    slugs = sorted(frags)
    print('Loaded %d fragments' % len(frags))
    print('\nPer-pillar counts:')
    for s in slugs:
        d = frags[s]
        print('  %s | concepts:%d formulas:%d refs:%d problems:%d connections:%d' % (
            s, len(d.get('concepts', [])), len(d.get('formulas', [])), len(d.get('references', [])),
            len(d.get('openProblems', [])), len(d.get('connections', []))))

    refs = merge_references(frags)
    jdump(CD + '/references.json', refs)
    with open(CD + '/references.bib', 'w') as f:
        f.write(bibtex(refs))

    formulas = merge_formulas(frags)
    jdump(CD + '/formulas.json', formulas)

    probs, prob_cands = merge_problems(frags)
    jdump(CD + '/open-problems.json', probs)

    nodes, edges = build_graph(frags)
    jdump(CD + '/concept-graph.json', {'nodes': list(nodes.values()), 'edges': list(edges.values())})

    cands = concept_merge_candidates(nodes)
    jdump(REVIEW + '/concept-merge-candidates.json', cands)
    jdump(REVIEW + '/problem-merge-candidates.json', prob_cands)

    conns, matrix = build_connections(frags, slugs)
    jdump(CD + '/connections.json', {'connections': conns, 'matrix': matrix})

    n_barely, hubs = write_digest(nodes, edges, refs, formulas, probs, conns)

    raw_refs = sum(len(d.get('references', [])) for d in frags.values())
    raw_form = sum(len(d.get('formulas', [])) for d in frags.values())
    print('\nRegistries written:')
    print('  references.json: %d unique (from %d raw) + references.bib' % (len(refs), raw_refs))
    print('  formulas.json: %d unique (from %d raw)' % (len(formulas), raw_form))
    print('  open-problems.json: %d (+%d fuzzy near-dup candidates flagged)' % (len(probs), len(prob_cands)))
    print('  concept-graph.json: %d nodes, %d edges' % (len(nodes), len(edges)))
    print('  connections.json: %d connections, %d barely explored' % (len(conns), n_barely))
    print('  _review/concept-merge-candidates.json: %d candidate pairs for judge' % len(cands))
    print('  top hubs: %s' % ', '.join(hubs[:8]))


def apply_merges():
    g = json.load(open(CD + '/concept-graph.json'))
    dec = json.load(open(REVIEW + '/merge-decisions.json'))
    nodes = {n['id']: n for n in g['nodes']}
    remap = {}
    for d in dec:
        keep = d['keep']
        for m in d.get('merge', []):
            if m == keep or m not in nodes or keep not in nodes:
                continue
            remap[m] = keep
            k, mn = nodes[keep], nodes.pop(m)
            k['aliases'] = sorted(set(k.get('aliases', []) + [m] + mn.get('aliases', [])))
            k['pillars'] = sorted(set(k['pillars']) | set(mn['pillars']))
            if len(mn.get('definition') or '') > len(k.get('definition') or ''):
                k['definition'] = mn['definition']

    def rm(x):
        seen = set()
        while x in remap and x not in seen:
            seen.add(x)
            x = remap[x]
        return x

    edges = {}
    for e in g['edges']:
        e['from'], e['to'] = rm(e['from']), rm(e['to'])
        if e['from'] == e['to']:
            continue
        k = (e['from'], e['to'], e['type'])
        if k in edges:
            p = edges[k]
            p['sourcePillars'] = sorted(set(p['sourcePillars']) | set(e['sourcePillars']))
            if len(e.get('description') or '') > len(p.get('description') or ''):
                p['description'] = e['description']
        else:
            edges[k] = e
    jdump(CD + '/concept-graph.json', {'nodes': list(nodes.values()), 'edges': list(edges.values())})

    # regenerate digest with merged graph + existing registries
    refs = json.load(open(CD + '/references.json'))
    formulas = json.load(open(CD + '/formulas.json'))
    probs = json.load(open(CD + '/open-problems.json'))
    conns = json.load(open(CD + '/connections.json'))['connections']
    write_digest(nodes, edges, refs, formulas, probs, conns)
    print('Applied %d merges; graph now %d nodes, %d edges; digest regenerated.' % (
        len(remap), len(nodes), len(edges)))


if __name__ == '__main__':
    if '--apply-merges' in sys.argv:
        apply_merges()
    else:
        main()
