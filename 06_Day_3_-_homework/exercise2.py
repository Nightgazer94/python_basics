def div():
    """
    Prompts the user to enter two natural numbers and divides the first by the second.

    The function performs the following checks:
    - Ensures both numbers are natural numbers (non-negative integers).
    - Handles division by zero.
    - Displays an error message if an invalid input is provided.

    Raises:
        ValueError: If either input is a negative integer.
        ZeroDivisionError: If the second number is zero.

    Returns:
        None
    """
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        if num1 < 0 or num2 < 0:
            raise ValueError("Only natural numbers (non-negative integers) are allowed.")
        result = num1 / num2
    except ValueError:
        print("Invalid input. Please enter natural numbers only.")
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
    else:
        print(f"The result is: {result}")

div()
