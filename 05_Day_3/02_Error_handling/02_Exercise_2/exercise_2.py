from random import randint

guessed = False
rnd = randint(1, 10)

while not guessed:
    try:
        str_num = int(input("Enter number:"))
    except ValueError:
        print("Please enter a number")
        continue

    num = str_num

    if num == rnd:
        print("Great!")
        guessed = True
    else:
        print("Wrong!")
