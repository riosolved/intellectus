import math

def is_perfect_square(number: int) -> bool:
    if number < 0:
        return False

    root = math.isqrt(number)

    return root * root == number



def is_perfect_cube(number: int) -> bool:
    if number < 0:
        return False
    
    root = round(math.pow(number, 1/3))

    return root * root * root == number


def is_magical(number: int) -> bool:
    return is_perfect_square(number) and is_perfect_cube(number)

def main():
    assert is_magical(1) == True   # 1^6 = 1
    assert is_magical(64) == True  # 2^6 = 64
    assert is_magical(16) == False # 16 is square but not cube
    assert is_magical(27) == False # 27 is cube but not square

    print("All checks passed.")

main()
