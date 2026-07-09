"""YOUR EXERCISE: the `run` command.

Goal - execute a solution file in its language's container:

    atk run interests/python/challenges/frosty_journey/code.py

The file's extension tells us the language; no --language flag needed.

Steps (each maps to something you saw in challenge.py):

1. Declare the command. This one takes an ARGUMENT, not an option -
   arguments are positional, options are named flags. The click piece:

       @click.argument("file", type=click.Path(exists=True, dir_okay=False, path_type=Path))

   - click.Path(exists=True) makes click verify the file exists and print
     a friendly error if not - no code needed from you.
   - path_type=Path hands your function a pathlib.Path instead of a str.
   - NOTE: arguments don't take help="..." (that's an option feature);
     describe the argument in the command's docstring instead.

2. Resolve the language from the extension:

       from atk.languages import by_path
       language_key, language = by_path(file)

   by_path raises ValueError for unknown extensions - decide how to
   surface that nicely (hint: catch it and `raise click.ClickException(str(err))`
   - click prints "Error: <message>" and exits with code 1).

3. Execute it: the language definition already knows how:

       ran_ok, output = language["run_code"](file)

   ran_ok is True (clean exit), False (crashed/failed), or None (could
   not execute at all, e.g. Docker is down).

4. Report. click.echo(output) prints the program output; click.secho lets
   you color a status line (fg="green" / "red" / "yellow" for the None
   case). Exit non-zero on failure so the command is scriptable:

       raise SystemExit(0 if ran_ok else 1)

5. Register the command in cli/__init__.py - see the TODO there.

Prove it works against an existing exercise before you start review.py:

    atk run interests/python/challenges/magic_numbers/code.py
"""

# your code here
