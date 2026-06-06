"""Environment smoke tests: the container must match the verified research env.

The 2026-06-06 deterministic reproduction (20/20 calc.py bit-identical) ran on
these exact library versions — see reports/2026-06-06-review.md §(f).
"""
import importlib

import pytest

PINNED = {
    "numpy": "2.4.4",
    "scipy": "1.17.1",
    "sympy": "1.14.0",
    "matplotlib": "3.10.9",
}


@pytest.mark.parametrize("pkg,version", sorted(PINNED.items()))
def test_pinned_version(pkg, version):
    mod = importlib.import_module(pkg)
    assert mod.__version__ == version, (
        f"{pkg} {mod.__version__} != verified {version} — "
        "update app/requirements.txt pin AND re-run the full reproduction "
        "(docker compose run --rm repro) before trusting results."
    )


def test_matplotlib_headless():
    import matplotlib

    assert matplotlib.get_backend().lower() == "agg"
