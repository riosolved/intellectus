#!/usr/bin/env bash

# Initialize a fresh clone of intellectus.
#
#   ./setup/initialize.sh
#
# Fixes what is safe to fix (venv, the atk command, the model, container
# images) and prints the install command for any system-level tool that
# is missing. Exit 0 means ready.

set -euo pipefail

SCRIPT_DIRECTORY="$(dirname "$0")"
cd "$SCRIPT_DIRECTORY/.."

MISSING=0

has_command() {
    command -v "$1" >/dev/null 2>&1
}

has_dependency() {
    local dependency="$1"
    local hint="$2"

    if has_command "$dependency"; then
        echo "[ok] $dependency installed"
    else
        echo "[!!] $dependency not found  ->  $hint"
        MISSING=1
    fi
}

has_dependency python "winget install --id Python.Python.3.13 -e"
has_dependency ollama "winget install --id Ollama.Ollama -e"
has_dependency nerdctl "winget install --id SUSE.RancherDesktop -e (select the containerd runtime on first launch)"

# --- the toolkit ------------------------------------------------------------

if has_command python; then
    if [ ! -d ".venv" ]; then
        python -m venv .venv
    fi

    source .venv/Scripts/activate

    pip install --quiet -e .
    echo "[ok] toolkit installed: atk"
fi

# --- the model ----------------------------------------------------------------

MODEL="qwen3-coder:30b"

if has_command ollama; then
    if ! ollama list | grep -q "$MODEL"; then
        ollama pull "$MODEL"
    fi
    echo "[ok] model: $MODEL"
fi

# --- the images ----------------------------------------------------------------

ENGINE="${ATK_CONTAINER_ENGINE:-}"
if [ -z "$ENGINE" ] && has_command nerdctl; then
    ENGINE="nerdctl"
fi

if [ -n "$ENGINE" ]; then
    python - <<'PYTHON'
from atk.runtime.images import ensure_image
from atk.runtime.runners import cpp, python

for image in (python.IMAGE, cpp.IMAGE):
    error = ensure_image(image)
    print(f"[!!] {error}" if error else f"[ok] image: {image}")
PYTHON
else
    echo "[!!] no container engine - images not built; code will not execute until nerdctl is installed"
    MISSING=1
fi

# --- summary --------------------------------------------------------------------

if [ "$MISSING" -eq 0 ]; then
    echo "DONE"
else
    echo "DONE (with missing dependencies - see [!!] lines above)"
    exit 1
fi
