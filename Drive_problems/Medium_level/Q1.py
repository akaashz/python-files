n = int(input())

valid = 0
invalid = 0
total = 0

for i in range(n):
    amount = int(input())

    if amount > 0 and amount % 100 == 0:
        valid += 1
        total += amount
    else:
        invalid += 1

print("Valid Requests:", valid)
print("Invalid Requests:", invalid)
print("Total Amount:", total)