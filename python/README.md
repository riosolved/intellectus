# Python Practice Gym

A small, fully-local loop for practicing Python: a model **generates** a
coding challenge, you **solve** it by hand, and the model **reviews** your
solution and hands back a `PASS` / `FAIL`. Everything runs offline against a
local [Ollama](https://ollama.com) model — no API keys, no internet.

```
  generate ──▶  python/<name>/challenge.py   (the task)
                        │
       you write ──▶  python/<name>/code.py   (your solution)
                        │
   review  ──▶  python/<name>/review.md       (feedback + PASS / FAIL)
```

## The two skills

Each skill's own doc has the flags, output, and details — this README just
ties them together.

| Skill | What it does | Docs |
|-------|--------------|------|
| **challenge** | Generates a fresh challenge for a topic + difficulty | [docs/challenge.md](docs/challenge.md) |
| **review** | Reviews your solution and returns a verdict | [docs/review.md](docs/review.md) |

## Layout

The tooling lives in `system/` at the repo root; your work lives under
`python/`. Run commands from the repo root, where both are visible.

```
intellectus/                 ← repo root (run commands from here)
├── system/                  ← the tooling
│   ├── llm.py               ← Ollama client (`ask`)
│   ├── requirements.txt
│   └── skills/
│       ├── challenge.py     ← generator
│       └── review.py        ← reviewer
└── python/
    ├── README.md            ← you are here
    ├── docs/                ← per-skill guides
    └── <name>/
        ├── challenge.py     ← the task (generated)
        ├── code.py          ← your solution (you write this)
        └── review.md        ← the review (generated)
```

## Setup (once)

Install [Ollama](https://ollama.com), pull the model, and start it:

```bash
ollama pull qwen3-coder:30b
ollama serve            # if it isn't already running
```

Then create the virtual environment and install dependencies:

```bash
python -m venv .venv
.venv/Scripts/pip.exe install -r system/requirements.txt
```

## The loop

Run everything from the **repo root** (`intellectus/`), as modules with `-m`
(see [why](#why--m-and-not-python-filepy) below). Each step links to its skill
doc for flags and details.

1. **Generate** a challenge — [challenge](docs/challenge.md):
   ```bash
   .venv/Scripts/python.exe -m system.skills.challenge --topic "generators" --difficulty "medium"
   ```
2. **Solve** it — write your answer in `python/<name>/code.py`, then run it
   directly (it's a plain script, so no `-m` needed):
   ```bash
   .venv/Scripts/python.exe python/<name>/code.py
   ```
   No output means your `assert`s passed; an `AssertionError` traceback means
   one failed.
3. **Review** it — [review](docs/review.md):
   ```bash
   .venv/Scripts/python.exe -m system.skills.review --exercise <name>
   ```

> **Shell note:** forward slashes are for Git Bash (MINGW64); PowerShell
> accepts backslashes (`.venv\Scripts\python.exe`) too.

## Why `-m` and not `python file.py`

Both skills import shared code from `system/llm.py` as `system.llm`. Running a
file directly only puts its own folder on Python's import path, so that import
fails. Running as a module from the repo root puts the root on the path, so
`system.llm` resolves. Use dotted module notation, no `.py` extension.

## Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| `ModuleNotFoundError: No module named 'system'` | Run from the wrong directory | `cd` to the repo root |
| `ModuleNotFoundError: No module named 'llm...'` | Old import in a skill | Use `from system.llm import ask` |
| `ConnectionError` / request fails | Ollama not running | Start it with `ollama serve` |
| `405` / `404` from the model call | Wrong Ollama URL | Endpoint should be `http://localhost:11434/api/generate` |
| `UnicodeEncodeError` on write | Windows default encoding | Write with `encoding="utf-8"` |
| Output lands under `system/` | Ran from inside `system/` | Run from the repo root |
