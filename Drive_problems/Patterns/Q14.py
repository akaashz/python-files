n = 5

for i in range(n):

    for j in range(2 * n - 1):

        if j == 0 or j == 2 * n - 2:
            print("*", end=" ")

        elif i == j and j <= n - 1:
            print("*", end=" ")

        elif i + j == 2 * n - 2 and j >= n - 1:
            print("*", end=" ")

        else:
            print(" ", end=" ")

    print()