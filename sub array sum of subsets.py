N = 8
A = [1, 2, 1, 3, 5, 2, 4, 2]

count = 0

for i in range(0, N - 2):
    first = A[i]
    second = A[i + 1]
    third = A[i + 2]

    if first + third == second:
        count = count + 1

print(count)