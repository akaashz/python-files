n = 5

for i in range(n):

    if i % 2 == 0:
        for j in range(n):
            print("*", end=" ")
    else:
        print(" ", end="")
        for j in range(n):
            print("*", end=" ")

    print()