l, r = map(int, input().split())

count = 0

for num in range(l, r + 1):

    total = 0

    for i in range(1, num):
        if num % i == 0:
            total += i

    if total == num and num != 0:
        count += 1

print("Perfect Number Count:", count)