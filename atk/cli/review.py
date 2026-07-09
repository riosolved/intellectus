"""YOUR EXERCISE: the `review` command.

Goal - review a solution file against the challenge that lives beside it:

    atk review interests/python/challenges/frosty_journey/code.py

This one is almost pure delegation - the pipeline already exists and takes
exactly the Path you'll receive:

    from atk.core.review import review as review_pipeline
    review_pipeline(file)

Steps:

1. Same @click.argument("file", ...) pattern as run.py. Careful with one
   thing: your click FUNCTION will be named `review` and the PIPELINE
   function is also named `review` - that's why the import above renames
   it. Name collisions between your command functions and what they call
   is a classic click gotcha.

2. Call the pipeline. Consider what should happen if the challenge file
   is missing next to the code file (solving a challenge that was never
   generated) - try it and see what error surfaces, then decide whether
   to catch it.

3. Register in cli/__init__.py.

Stretch goals, once the basics work:
- The pipeline prints a VERDICT banner; parse PASS/FAIL out and exit
  non-zero on FAIL, so the review is scriptable like run.
- A --topic option that gets woven into... no. Keep it thin. The stretch
  is the exit code.
"""

# your code here
