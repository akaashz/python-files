n = int(input())

valid = 0
invalid = 0
amount = 0

for _ in range(n):
    num = int(input())

    if num > 0 and num % 100 == 0:
        valid += 1
        amount += num
    else:
        invalid += 1

print(valid)
print(invalid)
print(amount)
