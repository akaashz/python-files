l, r = map(int, input().split())

count = 0

for num in range(l, r + 1):

    temp = num
    digits = 0

    while temp > 0:
        digits += 1
        temp //= 10

    temp = num
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    if total == num:
        count += 1

print("Armstrong Count:", count)