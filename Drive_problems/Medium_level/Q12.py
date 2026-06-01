a, b = map(int, input().split())

lcm = max(a, b)

while True:

    if lcm % a == 0 and lcm % b == 0:
        break

    lcm += 1

print("LCM:", lcm)