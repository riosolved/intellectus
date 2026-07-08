#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIRECTORY="$(dirname "$0")"

has_command() {
    command -v "$1" >/dev/null 2>&1
}

has_dependency() {
    local dependency="$1"

    if ! has_command "$dependency"; then
        echo "$dependency not found"
    else
        echo "$dependency installed"
    fi
}

has_dependency python
has_dependency pip
has_dependency ollama

if [ ! -d ".venv" ]; then
    python -m venv .venv
fi

source .venv/Scripts/activate

pip install -r "$SCRIPT_DIRECTORY/requirements.txt"

MODEL="qwen3-coder:30b"

export OLLAMA_MODELS="../models"
if ! ollama list | grep -q "$MODEL"; then
    ollama pull $MODEL
fi

echo "DONE"
