"""
STORY
    In a butterfly garden, each plant has a number of flowers. Some plants
    are special and have a prime number of flowers. You need to process
    the flower counts for a set of plants to determine which ones are
    special.

YOUR TASK
    1. `is_prime(n)` - takes an integer n and returns True if it is a prime
       number, False otherwise. A prime number is a whole number greater than
       1 that has no positive divisors other than 1 and itself.
    2. `special_plants(flowers)` - takes a list of integers representing
       flower counts for plants and returns a list of the flower counts for
       only those plants that have a prime number of flowers.

ASSERTS
    def main():
        # Test data
        plant_flowers = [4, 5, 6, 7, 8]

        # Assertions
        assert is_prime(2) == True
        assert is_prime(4) == False
        assert is_prime(5) == True
        assert is_prime(6) == False
        assert is_prime(7) == True
        assert special_plants(plant_flowers) == [5, 7]

        # Edge case
        assert is_prime(1) == False
        assert is_prime(0) == False

BACKGROUND
    A prime number is a natural number greater than 1 that has no positive
    divisors other than 1 and itself. For example:
    - 2 is prime because it's only divisible by 1 and 2.
    - 3 is prime because it's only divisible by 1 and 3.
    - 4 is not prime because it's also divisible by 2.
    - 1 is not considered prime by definition.

    List comprehensions in Python are a concise way to create lists. They
    follow the pattern:
        [expression for item in iterable if condition]
    This allows filtering and transformation of data in one line.

HINTS
    1. To check if a number is prime, you can test divisibility up to its square root.
    2. The `special_plants` function should use a list comprehension.
    3. Consider how to write a helper function that checks for primality.
    4. Remember that 0 and 1 are not prime numbers.

"""