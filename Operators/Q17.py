#to check if a number is a power of 2 using bitwise AND

a=int(input("Enter a number = "))  #8
if a & (a-1)==0:    #8 & 7 = 0 ==0
    print("given number is a power of 2")   
else:
    print("given number is not a power of 2")
