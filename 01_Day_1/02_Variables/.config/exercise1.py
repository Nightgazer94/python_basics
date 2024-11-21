temp = 15
temp_2 = "15"

# temp_2 is string that a different between temp(int) and temp_2(str)

# Addition
addition_result = temp + int(temp_2)

# or
try:
    addition_result2 = temp + temp_2
except TypeError as e:
    addition_result2 = str(e)

# Multiplication
multiplication_result = temp * temp_2

print(f"Addition result: {addition_result}")
print(f"Addition result: {addition_result2}")
print(f"Multiplication result: {multiplication_result}")

# about other actions iam sure they don't work we learn about that
# or we can convert temp_2 to int and all math operations will be available