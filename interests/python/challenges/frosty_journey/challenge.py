"""
STORY
    A frosty explorer is mapping out a journey across a snowy terrain. The
    explorer has a set of waypoints, each with an elevation and a temperature.
    Some waypoints are marked as "safe" or "dangerous". The explorer wants to
    compute the average temperature for safe waypoints, and raise an error if
    no safe waypoints exist.

YOUR TASK
    1. Define a function `compute_avg_temp(waypoints)` that:
       - Takes a dictionary where keys are waypoint names (strings) and values
         are dictionaries with 'elevation' (int), 'temperature' (float),
         and 'status' (string, either 'safe' or 'dangerous').
       - Returns the average temperature of all safe waypoints.
       - Raises a `ValueError` if there are no safe waypoints.

ASSERTS
    # Test data
    waypoints = {
        "camp_1": {"elevation": 1000, "temperature": -5.0, "status": "safe"},
        "camp_2": {"elevation": 1200, "temperature": -8.0, "status": "dangerous"},
        "camp_3": {"elevation": 900, "temperature": -3.0, "status": "safe"},
        "camp_4": {"elevation": 1100, "temperature": -6.0, "status": "dangerous"}
    }

    assert compute_avg_temp(waypoints) == -4.0

    # Test case: no safe waypoints
    waypoints_no_safe = {
        "camp_1": {"elevation": 1000, "temperature": -5.0, "status": "dangerous"},
        "camp_2": {"elevation": 1200, "temperature": -8.0, "status": "dangerous"}
    }

    try:
        compute_avg_temp(waypoints_no_safe)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass

BACKGROUND
    Dictionaries in Python are key-value stores. When you access a key that
    doesn't exist in a dictionary, it raises a KeyError unless you use the
    `.get()` method or handle it with `try/except`.

    A loop over a dictionary gives you its keys, not its values. You can loop
    over `.items()` to get both keys and values.

    The average of a list of numbers is the sum divided by the count.
    If there are no safe waypoints, you must raise an error — this is a
    requirement, not just a corner case.

HINTS
    - Loop through the dictionary to find all safe waypoints.
    - Accumulate temperatures and count for computing average.
    - Use a ValueError for invalid input like no safe waypoints.
    - Remember to check that you have at least one safe waypoint before
      computing the average.
"""