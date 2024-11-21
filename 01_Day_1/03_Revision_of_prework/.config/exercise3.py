import random

tree = ""
size = random.randint(3, 9)
print(f"Christmas tree size: {size}")

for _ in range(size):
    tree += "*"
    print(tree)
