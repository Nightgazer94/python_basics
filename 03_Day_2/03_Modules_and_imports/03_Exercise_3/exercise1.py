import random

def d6(num):
    return sum(random.randint(1, 6) for _ in range(num))


print(d6(10))