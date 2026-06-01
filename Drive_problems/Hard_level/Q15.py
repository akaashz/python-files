score, income, sports, attendance = input().split()

score = int(score)
income = int(income)
attendance = int(attendance)

if score >= 90 and income <= 250000 and attendance >= 85:
    print("Full Scholarship")

elif score >= 80 and sports in ["S", "I"] and attendance >= 80:
    print("Special Scholarship")

elif score >= 75 and income <= 500000:
    print("Partial Scholarship")

else:
    print("Not Eligible")