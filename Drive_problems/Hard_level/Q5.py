cutoff, score, category = input().split()

cutoff = float(cutoff)
score = int(score)

if category == "G":
    c = cutoff >= 85
    s = score >= 70

elif category == "OBC":
    c = cutoff >= 80
    s = score >= 65

elif category == "SC":
    c = cutoff >= 70
    s = score >= 55

elif category == "ST":
    c = cutoff >= 65
    s = score >= 50

else:
    print("Invalid Category")
    exit()

if c and s:
    print("Eligible")
elif c or s:
    print("Waiting List")
else:
    print("Not Eligible")