# TODO — draft-06 (discrete-program limits / map of negatives)

Internal AI-assisted draft. **Never submit without human review.** The DRAFT banner on draft.md line 1 must stay until a human signs off.

## Status
- v0.1 (2026-06-09): first assembly of the three second-arc negatives into a single negative-results note. Synthesizes existing findings only; no new claims, no new arXiv IDs. Statuses verbatim from findings.json.

## Human-review checklist (before any release)

### Critical
- [ ] **References.** The draft cites repo-present IDs by number; but the trace-anomaly↔EE convention references (Casini–Huerta–Myers "sphere EE = a"; Solodukhin "log coefficient ~ c"), and the Bisognano–Wichmann / Unruh textbook conventions of Wall 2, are cited **without verified arXiv IDs** (flagged in §References). A human must supply and verify each ID against arXiv, or cite the canonical book/journal references, before release. NEVER invent an ID.
- [ ] **No overclaim of "no-go".** Confirm every wall is framed as a negative of the *specific finite-N surrogate construction* (§6 Limits), not a theorem. The abstract and §7 must not read as universal impossibility.
- [ ] **Numbers vs findings.** Cross-check each quantitative claim against the cited finding + its results.json: Wall 1 (F-031 ρ^0.49/ρ^1.0; F-037 +0.386 identical ξ=1/6 vs 0; F-038 ρ^0.656, Fano 3.7→5.3); Wall 2 (F-036 boost slope 29.2 R²=0.97, Unruh off 52%; F-033 Connes corr 0.319 R²=0.10 — note: deterministic 16-pair value after the kolo-21 reproducibility fix, NOT the old 0.098); Wall 3 (F-039 c_EE=7.562, scalar −3 off 152%, −18/11 off 362%).

### Major
- [ ] **Wall 1 ↔ draft-04 consistency.** draft-04 §4.3 already states the 4D quantitative area-law is absent (F-031) and distinguishes it from the slab truncated-SSEE area law (F-019). Ensure draft-06 does not contradict draft-04 and that the slab/dS distinction is consistent across both.
- [ ] **Is a negative-results letter the right venue?** Decide whether this is a standalone letter, an appendix to draft-04, or an internal note only. Negative results are publishable but venue-sensitive.
- [ ] **Wall 2 forward pointer.** The "non-surrogate geometric-boost Dirac with γ5" is named as the missing ingredient; if that compute is later run, fold its result here.

### Minor
- [ ] Title/slug: `draft-06-discrete-program-limits` is descriptive; consider a sharper title for a letter.
- [ ] Decide whether to include the positives (§3) inline or cite the companion drafts (draft-01/02/04) instead.

## Open compute that would change this draft
- Wall 1: exact curved 4D de Sitter propagator (breaks the surrogate's volumetric S_full).
- Wall 2: non-surrogate Dirac from the geometric Killing boost ξ=x∂_t+t∂_x with chiral grading γ5 (the only path to a non-tautological Unruh 2π).
- Wall 3: a continuum-limit, regulator-independent universal EE coefficient (anomaly-sensitive rather than κ-cutoff-sensitive).
