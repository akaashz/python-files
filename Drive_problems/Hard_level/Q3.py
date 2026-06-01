temp, oxygen, heart, age = map(int, input().split())

if oxygen < 90 or temp >= 104 or heart > 130:
    print("Critical")

elif age >= 60 and (oxygen < 94 or temp > 100 or heart > 110):
    print("High Risk")

elif oxygen < 96 or temp > 99 or heart > 100:
    print("Observation")

else:
    print("Normal")