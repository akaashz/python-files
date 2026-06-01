vehicle, hours, member = input().split()
hours = int(hours)

if vehicle == "C":
    fee = 40
    if hours > 2:
        fee += (hours - 2) * 30

elif vehicle == "B":
    fee = 20
    if hours > 2:
        fee += (hours - 2) * 10

elif vehicle == "T":
    fee = 80
    if hours > 2:
        fee += (hours - 2) * 50

else:
    print("Invalid Vehicle")
    exit()

if member == "Y" and fee >= 200:
    fee = int(fee * 0.8)

print(fee)