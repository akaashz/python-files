score, income, emi, loan, emp = input().split()

score = int(score)
income = int(income)
emi = int(emi)
loan = int(loan)

ratio = emi * 100 / income

if score < 600 or ratio > 60:
    print("Rejected")

elif emp == "B":
    if score >= 780 and ratio <= 40 and loan <= income * 20:
        print("Approved")
    else:
        print("Manual Review")

else:
    if score >= 750 and ratio <= 40 and loan <= income * 20:
        print("Approved")
    else:
        print("Manual Review")