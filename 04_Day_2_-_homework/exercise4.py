def find_boundaries(numbers):
    if not numbers:
        return None

    filtered_numbers = [num for num in numbers if isinstance(num, (int, float))]

    if not filtered_numbers:
        return None

    smallest = min(filtered_numbers)
    largest = max(filtered_numbers)

    return (smallest, largest)

print(find_boundaries([1, 2, 3, 4, 5]))
