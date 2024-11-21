def divide(a, b):
    try:
        if not (isinstance(a, int) and isinstance(b, int)) or a <= 0 or b <= 0:
            return None
        return a / b
    except ZeroDivisionError:
        return None


print(divide(0, 5))