n = int(input())

low = 0
normal = 0
high = 0

for i in range(n):
    units = int(input())

    if units < 100:
        low += 1
    elif units <= 300:
        normal += 1
    else:
        high += 1

print("Low:", low)
print("Normal:", normal)
print("High:", high)