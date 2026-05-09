# year validator.py
"""Module that validates leap years."""


def is_leap_year(year: int) -> bool:
    """
    Determine if a year is a leap year.

    A year is a leap year if:
    - It is divisible by 400, OR
    - It is divisible by 4 AND is not divisible by 100.

    Args:
        year: The year to validate (integer).

    Returns:
        True if the year is a leap year.
        False if it is not a leap year.

    Examples:
        >>> is_leap_year(2000)
        True
        >>> is_leap_year(1900)
        False
        >>> is_leap_year(2024)
        True
    """
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def main() -> None:
    "Main function. In and Out of the user."
    year = int(input("Type the year that you want to verify: "))

    if is_leap_year(year):
        print(f"The {year} year is a leap year.")
    else:
        print(f"The {year} year is not a leap year")


if __name__ == "__main__":
    main()
