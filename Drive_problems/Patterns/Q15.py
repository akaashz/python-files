n = 5

for i in range(1, n):

    for j in range(n - i):
        print("  ", end="")

    for j in range(i):
        print("* ", end="")

    for j in range(i):
        print("* ", end="")

    print()