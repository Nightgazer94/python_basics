array = [23, 45, 12, 78, 90, 34, 21, 65, 87, 54]

max_value = array[0]
for i in range(1, len(array)):
    if array[i] > max_value:
        max_value = array[i]

print(max_value)