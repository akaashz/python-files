#to find the leap year

n=int(input("Enter a year: "))

if n%4==0 and n%400==0 and n%100!=0:
    print("Leap year")
else:
    print("Not a leap year")

#to find the type of triangle

a=int(input())
b=int(input())
c=int(input())

if a+b>c or b+c>a or c+a>b:
    print("Triangle can be formed")

    if a==b and b==c:
        print("Equilateral")
    elif a==b or b==c or c==a:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Not a Valid Triangle")

#units=500
#first 100 units free (0-100)
#100-300----->5rs/unit
#300-500----->10rs/unit
#above 500----->15rs/unit

#for 500 units apply extra charges ---> 200rs
#450-100 --> 350

units=int(input("Enter the number of units consumed : "))
if units<=100:
    print("Total bill is : 0")
elif units>100 and units<=300:
    bill=(units-100)*5
    print("Total bill is : ",bill)
elif units>300 and units<=500:
    bill=(200*5)+(units-300)*10  #200*5=1000--->1000+(500-300)*10=1000+2000=3000
    print("Total bill is : ",bill)  
else:
    bill=(200*5)+(200*10)+(units-500)*15
    print("Total bill is : ",bill)

'''
leap year condition:
    month=2-->29 days
else:
    28 days

1,3,5,7,8,10,12-->31 days
4,6,9,11-->30 days

'''
year=int(input("Enter a year: "))
month=int(input("Enter a month: "))

if month==2:
    if year%4==0 and year%400==0 and year%100!=0:
        print("29 days")
    else:
        print("28 days")
elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    print("31 days") 
else:
    print("30 days")       

