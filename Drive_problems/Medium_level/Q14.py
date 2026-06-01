n, d = map(int, input().split())

count = 0

if n == 0 and d == 0:
    count = 1

while n > 0:

    digit = n % 10

    if digit == d:
        count += 1

    n //= 10

print("Frequency:", count)