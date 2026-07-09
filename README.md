# The Autodidact's Toolkit

A fully local practice gym plus a collection of exercises and knowledge.

The **toolkit** (`atk`) drives the practice loop: a local LLM generates a
machine-verified coding challenge, you solve it by hand, your code runs in
an isolated container, and the LLM reviews it with a `PASS` / `FAIL`
verdict. No API keys, no internet, nothing executes directly on your
machine.

```bash
atk challenge --topic "generators" --difficulty medium --language python
```

Fresh clone? Run `./setup/initialize.sh` (Git Bash) - it checks every prerequisite, sets
up what it safely can, and tells you exactly what's missing
([getting started](documentation/getting-started.md)).

## Documentation

| Doc | Covers |
|-----|--------|
| [Getting started](documentation/getting-started.md) | Setup (Ollama, container engine, install) and the practice loop |
| [challenge](documentation/challenge.md) | Generating machine-verified challenges |
| [review](documentation/review.md) | Running and grading your solutions |
| [Containers](documentation/containers.md) | The containerd-first execution strategy and registered images |
| [Adding a language](documentation/adding-a-language.md) | The manual checklist for supporting a new language |

## Layout

```
intellectus/
|-- README.md            <- you are here
|-- pyproject.toml       <- packaging; installs the `atk` command
|-- setup/               <- initialize.sh (fresh-clone bootstrap)
|-- documentation/       <- all toolkit documentation
|-- atk/                 <- the toolkit (cli / core / languages / runtime)
`-- interests/           <- everything you practice
    |-- python/          <- challenges/
    |-- c++/             <- challenges/ + hand-collected exercises/
    `-- sql/             <- challenges/ + exercises/ + knowledge notes
```

## Interests

Alongside the generated challenges, each interest folder holds exercises
gathered from sources like LeetCode, CodeWars, HackerRank, and technical
screenings - plus, for SQL, a personal knowledge base
([joins](interests/sql/knowledge/joining/README.md),
[performance](interests/sql/knowledge/performance/README.md)) and a
[MySQL sandbox setup](interests/sql/setup.md).
