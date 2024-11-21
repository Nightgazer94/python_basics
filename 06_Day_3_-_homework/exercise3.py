def validate_isbn(isbn):
    """
    Validates a 13-digit ISBN number.

    Args:
        isbn (str): The ISBN number as a string of 13 digits.

    Returns:
        bool: True if the ISBN is valid, False otherwise.
    """
    if len(isbn) != 13 or not isbn.isdigit():
        return False

    total = 0
    for i, digit in enumerate(isbn[:-1]):
        num = int(digit)
        if i % 2 == 0:
            total += num
        else:
            total += num * 3

    check_digit = (10 - (total % 10)) % 10
    return check_digit == int(isbn[-1])

print(validate_isbn("9780306406157"))
print(validate_isbn("9780306406158"))

