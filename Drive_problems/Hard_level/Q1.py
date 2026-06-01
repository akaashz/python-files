age, income = map(int, input().split())

if age < 60:

    if income <= 250000:
        tax = 0
    elif income <= 500000:
        tax = (income - 250000) * 5 // 100
    elif income <= 1000000:
        tax = 12500 + (income - 500000) * 20 // 100
    else:
        tax = 112500 + (income - 1000000) * 30 // 100

else:

    if income <= 300000:
        tax = 0
    elif income <= 500000:
        tax = (income - 300000) * 5 // 100
    elif income <= 1000000:
        tax = 10000 + (income - 500000) * 20 // 100
    else:
        tax = 110000 + (income - 1000000) * 30 // 100

print(tax)