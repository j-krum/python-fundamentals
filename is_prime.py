# is_prime.py
"""Module that validades prime numbers"""


def is_prime(number: int) -> bool:
    """
    Determine if a number is prime or not.

    A number is prime if:
    - Is and integer.
    - It must be a natural number.
    - It must be greater than 1.
    - Is divisible by 1 AND by himself

    Args:
        number (int): The number to check (integer).

    Returns:
        True: If the number is prime.
        False: If the number isn't prime.

    Examples:
        >>> is_prime(1.2)
        False
        >>> is prime (-1)
        False
        >>> is_prime(0)
        False
        >>> is_prime(1)
        False
        >>> is_prime(2)
        True
        >>> is_prime(3)
        True
    """
    if not isinstance(number, int):
        return False
    elif isinstance(number, str):
        return False
    elif isinstance(number, float):
        return False
    elif number <= 1:
        return False
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
        else:
            return True


def main() -> None:
    """User input and output"""
    number = int(input("Type the number that you want to verify: "))

    if is_prime(number):
        print(f"The number {number} IS prime")
    else:
        print(f"The number {number} IS NOT prime.")


if __name__ == "__main__":
    main()
