# Agent rules for intellectus

Rules for AI agents (and humans) working in this repository. Read the
relevant doc in `documentation/` before changing a subsystem.

## Containerfiles - exactly alpine, mandatory

Every Containerfile in `atk/runtime/containerfiles/` MUST start
`FROM alpine:<version>` - exactly alpine, not `-alpine` variants of other
images (`python:3.13-alpine` is NOT allowed), not debian/ubuntu/slim. The
Containerfile then sets up the language's environment explicitly with
`apk add --no-cache ...` (interpreter, compiler, package manager - e.g.
python3 + py3-pip for Python). If a toolchain seems to need a non-alpine
base, raise it instead of switching bases.

Images are throwaway runtimes, not dev environments. Per-exercise Python
dependencies are never installed at run time - they are baked into a
derived image keyed by the requirements.txt hash (see
`ensure_requirements_image`). Full rules: [documentation/containers.md](documentation/containers.md).

## Other invariants

- The container engine is containerd via `nerdctl` only; the sole escape
  hatch is the user setting `ATK_CONTAINER_ENGINE` themselves. Do not add
  fallback engine detection.
- Generated and student code never executes on the host - always through
  `atk/runtime/` (one runner module per language in runtime/runners/).
- Challenges must be machine-verified before saving (reference solution
  proves the acceptance checks); never weaken this gate.
- Adding a language is deliberately manual - follow
  [documentation/adding-a-language.md](documentation/adding-a-language.md); do not build
  auto-registration.
- `atk/cli/run.py` and `atk/cli/review.py` are the user's own click
  practice exercises - do not implement them.
