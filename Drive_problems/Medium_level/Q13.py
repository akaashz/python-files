n, k = map(int, input().split())

violations = 0
highest = 0

for i in range(n):

    amount = int(input())

    if amount > k:
        violations += 1

    if amount > highest:
        highest = amount

print("Violations:", violations)
print("Highest Transaction:", highest)