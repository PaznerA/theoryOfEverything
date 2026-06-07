"""pytest conftest for the toe library test-suite.

Single responsibility: put the in-repo lib/ directory (resolved __file__-
relative, two levels up from app/tests/) on sys.path so that `import toe`
(and `import toe.fits`, etc.) resolve to the
composable library under lib/toe/ WITHOUT requiring an editable install.

The toe package deliberately ships no setup.py / pyproject; it is imported by
path. Every test_toe_<module>.py relies on this shim. Keep it dependency-free
and import-time cheap (no numpy/sympy here) so collection stays fast.
"""

import os
import sys

# This file lives at <repo>/app/tests/conftest.py.
# lib/ is two levels up from app/tests/, then into "lib".
_HERE = os.path.dirname(os.path.abspath(__file__))
_REPO_ROOT = os.path.abspath(os.path.join(_HERE, os.pardir, os.pardir))
_LIB_DIR = os.path.join(_REPO_ROOT, "lib")

if _LIB_DIR not in sys.path:
    # prepend so the in-repo toe/ wins over any same-named installed package
    sys.path.insert(0, _LIB_DIR)
