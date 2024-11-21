def div(num1, num2):
    return [num for num in range(num1, num2+1) if num % 2 == 0 and num % 3 != 0]

a = div(1, 20)
print(a)




