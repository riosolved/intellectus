"""Isolated execution of generated and student code.

Four layers, one concept each - study them in this order:

1. engine.py    how the toolkit talks to containerd (shelling out to
                nerdctl); every runtime action reduces to one CLI command.
2. images.py    frozen filesystems built from recipes: the registered
                per-language Containerfiles, and derived images that bake
                an exercise's dependencies in.
3. sandbox.py   the cage every run lives in: read-only mount, no network,
                destroyed on exit.
4. runners/     the public face - one module per language; what a
                language module plugs into.

Data lives beside the code: containerfiles/ holds one recipe per language.
"""
