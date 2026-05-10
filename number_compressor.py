# number_compressor.py
"""Module that compresses numbers"""


def number_compressor(num1: int, num2: int, num3: int) -> int:
    """
    The objective is to concatenate 3 integers into one
    unique number.

    To compress 3 numbers:
        - The source numbers must be natural numbers.
        - The source numbers must be from 0 to 9.
        - The compressed number must have 3 digits.

    Args:
        - num1: integer from 0 to 9
        - num2: integer from 0 to 9
        - num3: integer from 0 to 9

    Returns:
        - Compressed number of 3 digits.

    Examples:
        >>> number_compressor(1,2,3)
        123
        >>> number_compressor(10,2,3)
        ValueError
        >>> number_compressor(1.5,2,3)
        ValueError
        >>> number_compressor(a,b,3)
        ValueError
        >>> number_compressor(-1,1,3)
        ValueError
    """
    # Guard 1: all three integers
    if (
        not isinstance(num1, int)
        or not isinstance(num2, int)
        or not isinstance(num3, int)
    ):
        raise ValueError("All inputs must be integers.")
    # Guard 2: all three are single digits (0-9)
    if not (0 <= num1 <= 9) or not (0 <= num2 <= 9) or not (0 <= num3 <= 9):
        raise ValueError("All inputs must be single digits (0-9)")
    # Compress
    return int(str(num1) + str(num2) + str(num3))


def main() -> None:
    """User I/O"""
    # Testing first number.
    while True:
        try:
            num1 = int(input("Enter the first digit (0-9): "))
            if not (0 <= num1 <= 9):
                raise ValueError("Digit must be between 0 and 9.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Try again")
    # Testing second number.
    while True:
        try:
            num2 = int(input("Enter the second digit (0-9): "))
            if not (0 <= num2 <= 9):
                raise ValueError("Digit must be between 0 and 9.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Try again")
    # Testing third number.
    while True:
        try:
            num3 = int(input("Enter the third digit (0-9): "))
            if not (0 <= num3 <= 9):
                raise ValueError("Digit must be between 0 and 9.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Try again")
    # Compressing the numbers
    result = number_compressor(num1, num2, num3)
    print(f"Compressed number: {result}")
