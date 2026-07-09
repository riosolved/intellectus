"""The atk CLI - the single entry point for the practice loop.

Installed as the `atk` command (with `intellectus` as an alias) via
pyproject.toml:
    [project.scripts]
    atk = "atk.cli:cli"
    intellectus = "atk.cli:cli"
Each line means: run the `cli` object in this module. Click does the rest.

STATUS: work in progress.
- `challenge` is fully wired - study it in cli/challenge.py, it is the
  worked example for the pattern.
- `run` and `review` are YOURS to build: see the guided TODOs in
  cli/run.py and cli/review.py.
"""

import click

from atk.cli.challenge import challenge


@click.group()
def cli():
    """The autodidact's toolkit: generate, run, and review challenges."""


cli.add_command(challenge)

# TODO(you): once you have written them, register your commands the same way:
#
#   from atk.cli.run import run
#   from atk.cli.review import review
#
#   cli.add_command(run)
#   cli.add_command(review)
