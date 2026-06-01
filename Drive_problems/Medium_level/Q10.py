p, d, m = map(float, input().split())

for i in range(int(m)):
    p = p - (p * d / 100)

print("Final Price:", format(p, ".2f"))