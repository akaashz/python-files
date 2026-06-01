l, r = map(int, input().split())

count = 0

for num in range(l, r + 1):

    if num > 1:
        prime = True

        for i in range(2, num):
            if num % i == 0:
                prime = False
                break

        if prime:
            count += 1

print("Prime Count:", count)