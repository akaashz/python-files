amount, daily_spent, card_limit, country, pin = input().split()

amount = int(amount)
daily_spent = int(daily_spent)
card_limit = int(card_limit)

if pin == "W":
    print("Declined")

elif amount + daily_spent > card_limit:
    print("Declined")

elif amount > 50000 or (country == "F" and amount > 20000):
    print("Flagged")

else:
    print("Approved")