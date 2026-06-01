n = 5

for i in range(1, n + 1):

    if i % 2 == 1:
        for j in range(i):
            print((i + 1)//2, end=" ")
    else:
        for j in range(i):
            print("*", end=" ")

    print()