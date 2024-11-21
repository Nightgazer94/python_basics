a = [1, 3, 7, 8, 3, 4, 3, 6]
x = 3
positions = []

for i in range(len(a)):
    if a[i] == x:
        positions.append(i)

print(positions)



