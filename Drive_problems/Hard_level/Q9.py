score, tab, face, disconnect = map(int, input().split())

if score < 35:
    print("Failed")

elif tab > 5 or face > 3 or disconnect > 10:
    print("Result Withheld")

elif (tab > 0 or face > 0 or disconnect > 0) and score >= 80:
    print("Manual Verification")

else:
    print("Passed")