meal_type, amount, membership = input().split()

amount = int(amount)
membership = int(membership)

if meal_type not in ["V", "N"]:
    print("Invalid Meal")

else:

    if meal_type == "V" and amount > 1000:
        amount = amount * 90 / 100

    elif meal_type == "N" and amount > 1500:
        amount = amount * 88 / 100

    if membership == 1:
        amount = amount * 95 / 100

    elif membership == 2:
        amount = amount * 92 / 100

    print(int(amount))