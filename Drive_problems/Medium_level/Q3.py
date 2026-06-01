n, k = map(int, input().split())

total = 0
count = 0

for i in range(n):
    fee = int(input())

    total += fee

    if fee > k:
        count += 1

print("Total Collection:", total)
print("Above Expected:", count)