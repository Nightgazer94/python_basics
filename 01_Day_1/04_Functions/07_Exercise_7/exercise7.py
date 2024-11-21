def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def iterate_through(number):
    for i in range(number):
        if is_even(i):
            print(i)
        else:
            continue

iterate_through(15)

