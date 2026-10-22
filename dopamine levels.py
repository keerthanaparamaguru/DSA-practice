N = 5
L = 3
R = 6
A = [4, 8, 3, 2, 5]

level = 0
highest = 0
lowest = 0

for x in A:
    if x >= L and x <= R:
        level = level + 1
    else:
        level = level - 1

    if level > highest:
        highest = level

    if level < lowest:
        lowest = level

print(highest, lowest)