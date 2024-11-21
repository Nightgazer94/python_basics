def square(x):
    return x**2

def square_print(x):
    print(f"{x} is squared {square(x)}")

a =(square(10)) + 10
print(a)

# we can't make None + 10
# b = square_print(10) + 10
# print(b)

