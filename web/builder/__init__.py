"""Builder package for the Theory of Everything presentation site.

A minimalist, pure-python static-site generator that renders a *view* of the
repository directly from its existing markdown + JSON registries. The site is
never a copy that can drift: every run deletes and rebuilds ``web/dist/`` from
the live source files.
"""
