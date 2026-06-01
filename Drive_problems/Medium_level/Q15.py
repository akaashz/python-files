s, inc, t = map(int, input().split())

days = 0
total = 0
daily = s

while total < t:

    total += daily
    days += 1
    daily += inc

print("Days Required:", days)