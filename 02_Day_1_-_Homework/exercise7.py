def histogram(numbers):
    if not all(isinstance(num, int) for num in numbers):
        return None

    result = ""
    for num in numbers:
        line = ""
        for _ in range(num):
            line += "#"
        result += line + "\n"

    return result

h = histogram([2, 6, 3, 1])
print(h)

h = histogram([1, 2, 'Hello!'])
print(h)

