age, premium, smoker, history = input().split()

age = int(age)
premium = int(premium)

if age < 18 or age > 80:
    print("Not Eligible")

else:

    final = premium

    if 45 <= age <= 60:
        final += premium * 20 // 100

    elif age > 60:
        final += premium * 35 // 100

    if smoker == "Y":
        final += premium * 25 // 100

    if history == "Y":
        final += premium * 30 // 100

    if smoker == "Y" and history == "Y":
        final += final * 15 // 100

    print(final)