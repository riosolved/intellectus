"""The worked example command. Study this shape, then build run and review.

Anatomy of a click command:

- @click.command() turns a plain function into a Command. Its NAME becomes
  the subcommand (`atk challenge`), its DOCSTRING becomes the
  --help text. You get help screens for free - that's most of why click.

- @click.option("--topic", ...) declares a named flag. Each option becomes
  a keyword argument to the function, matched by name (topic, difficulty,
  language). `required=True` makes click reject the call with a clear
  error before your code even runs.

- type=click.Choice([...]) restricts the value to a fixed set AND
  documents the choices in --help. Note the language choices come straight
  from the registry - add a language module and the CLI learns it without
  edits here.

- show_default=True prints the default in --help. Small flag, big
  discoverability win.

The function body is one line. That is the point: the CLI layer parses and
validates, the core layer does the work. Keep yours that thin too.
"""

import click

from atk.core.generation import generate
from atk.languages import LANGUAGES


@click.command()
@click.option("--topic", required=True, help="The feature or theme to drill.")
@click.option(
    "--difficulty",
    type=click.Choice(["beginner", "medium", "hard"]),
    default="medium",
    show_default=True,
    help="How hard it should be.",
)
@click.option(
    "--language",
    type=click.Choice(list(LANGUAGES)),
    default="python",
    show_default=True,
    help="Which language to generate for.",
)
def challenge(topic: str, difficulty: str, language: str):
    """Generate a new, machine-verified challenge."""
    generate(topic, difficulty, language)
