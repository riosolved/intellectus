# Getting started

The autodidact's toolkit (`atk`) is a fully local practice gym: a local
LLM **generates** a coding challenge, you **solve** it by hand, your code
**runs** in an isolated container, and the LLM **reviews** your solution
with a `PASS` / `FAIL` verdict. No API keys, no internet, nothing executes
directly on your machine.

```
  generate --> interests/<language>/challenges/<name>/challenge.*   (the task)
                        |
   you write --> interests/<language>/challenges/<name>/code.*      (your solution)
                        |
   review  --> interests/<language>/challenges/<name>/review.md     (feedback + PASS / FAIL)
```

## Setup (once)

From a fresh clone, the initialization script checks every prerequisite,
fixes what is safe to fix (venv, the `atk` command, prebuilt images), and
prints exact commands for what it won't install silently:

```bash
./setup/initialize.sh
```

It reports each dependency as `[ok]` or `[!!]` with the exact winget
command for anything missing; exit code 0 means ready. What it checks,
piece by piece:

**1. Ollama** - the local LLM that generates and reviews:

```bash
ollama pull qwen3-coder:30b
ollama serve            # if it isn't already running
```

**2. containerd + nerdctl** - all generated and student code executes in
throwaway containers on containerd, driven through `nerdctl`. On Windows,
install [Rancher Desktop](https://rancherdesktop.io) with the containerd
runtime selected. (Explicit override: `ATK_CONTAINER_ENGINE=<cli>` accepts
any docker-flag-compatible CLI.) Images are built automatically on first
use from the Containerfiles registered in `atk/runtime/containerfiles/`
(alpine-based, thin).

**3. The toolkit** - create the venv and install editable:

```bash
python -m venv .venv
.venv/Scripts/pip.exe install -e .
```

This installs the `atk` command (alias: `intellectus`) into the venv.

## The loop

Run from the repo root:

1. **Generate** a challenge - see [challenge.md](challenge.md):
   ```bash
   .venv/Scripts/atk.exe challenge --topic "generators" --difficulty medium --language python
   ```
2. **Solve** it - write your answer in `interests/<language>/challenges/<name>/code.*`.
3. **Run and review** - `atk run <file>` and `atk review <file>` are being
   built (guided TODOs in `atk/cli/run.py` and `atk/cli/review.py`).
   Until then, the review pipeline is callable directly - see
   [review.md](review.md):
   ```bash
   .venv/Scripts/python.exe -c "from pathlib import Path; from atk.core.review import review; review(Path('interests/python/challenges/<name>/code.py'))"
   ```

> **Shell note:** forward slashes are for Git Bash (MINGW64); PowerShell
> accepts backslashes (`.venv\Scripts\atk.exe`) too.

## Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| `atk: command not found` | Toolkit not installed into the venv | `.venv/Scripts/pip.exe install -e .` from the repo root |
| `ConnectionError` / request fails | Ollama not running | Start it with `ollama serve` |
| `405` / `404` from the model call | Wrong Ollama URL | Endpoint should be `http://localhost:11434/api/generate` |
| `WARNING: saving UNVERIFIED challenge` | Container engine not running | Start Rancher Desktop (or your `ATK_CONTAINER_ENGINE`) and re-run |
| `nerdctl (containerd) not found on PATH` | nerdctl not installed | Install Rancher Desktop (containerd runtime), or set `ATK_CONTAINER_ENGINE` explicitly |
| `UnicodeEncodeError` on write | Windows default encoding | Write with `encoding="utf-8"` |
