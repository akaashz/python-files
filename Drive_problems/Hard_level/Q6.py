failed, device, location, otp = input().split()

failed = int(failed)

if failed >= 5:
    print("Blocked")

elif device == "U" and location == "R":

    if otp == "Y":
        print("OTP Required")
    else:
        print("Blocked")

elif device == "U" or location == "R":
    print("OTP Required")

else:
    print("Login Allowed")