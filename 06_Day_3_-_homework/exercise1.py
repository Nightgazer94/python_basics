import random

def random_average(n):
    """
    Calculates the average of n random numbers in the range from 0 to 101.

    Args:
        n (int): The number of random numbers to calculate the average for.

    Returns:
        float: The average value of the generated numbers.
    """
    numbers_list = [random.randint(0, 101) for _ in range(n)]
    sum_of_numbers = sum(numbers_list) / n
    return sum_of_numbers

print(random_average(7))
