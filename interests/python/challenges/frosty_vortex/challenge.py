"""
STORY
    A wizard's apprentice is tasked with formatting spell names and their associated mana costs for a magical journal. The apprentice must format the data into a human-readable string, ensuring consistent spacing and alignment. If an invalid mana cost is provided (negative or not a number), an error must be raised.

YOUR TASK
    1. format_spell(spell_name: str, mana_cost: float) -> str
        - Takes a spell name and its mana cost.
        - Returns a formatted string like "Spell: [spell_name], Mana: [mana_cost]".
        - The mana cost should be displayed with exactly two decimal places.
        - Raises ValueError if mana_cost is negative or not a number.

ASSERTS
    def main():
        # Test data
        spells = [
            ("Fireball", 15.75),
            ("Heal", 8.2),
            ("Lightning Bolt", 22.0)
        ]

        # Expected outputs
        expected = [
            "Spell: Fireball, Mana: 15.75",
            "Spell: Heal, Mana: 8.20",
            "Spell: Lightning Bolt, Mana: 22.00"
        ]

        results = []
        for name, cost in spells:
            results.append(format_spell(name, cost))

        assert results == expected

        # Test invalid input
        try:
            format_spell("Invisible", -5.0)
            assert False, "Should have raised ValueError"
        except ValueError:
            pass  # Expected

        try:
            format_spell("Magic", "not_a_number")
            assert False, "Should have raised ValueError"
        except ValueError:
            pass  # Expected

BACKGROUND
    String formatting is the process of creating a string from data by inserting values into placeholders. In Python, you can use f-strings (formatted string literals) or the .format() method to do this.

    A decimal number like 15.75 can be displayed with exactly two digits after the decimal point using format specifiers like :.2f. This ensures consistent output for monetary or measurement values.

    The ValueError exception is Python's way of signaling that something went wrong in a program, such as invalid input.

    A function in Python can raise an exception (like ValueError) using the `raise` keyword when it encounters a condition it cannot handle.

HINTS
    1. You can use the format specifier :.2f to ensure two decimal places.
    2. Check if the mana_cost is a number and non-negative before formatting.
    3. Use str() or f-strings for building the final output string.
    4. Use `isinstance()` or try/except blocks to validate input types.

"""