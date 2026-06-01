distance, class_type, age, booking = input().split()

distance = int(distance)
age = int(age)

if class_type == "G":
    fare = distance * 1

elif class_type == "S":
    fare = distance * 2

elif class_type == "A":
    fare = distance * 4

else:
    print("Invalid Class")
    exit()

if age < 5:
    fare = 0

elif age >= 60:
    fare = fare * 60 // 100

if booking == "O":
    fare = fare * 95 // 100

print(fare)