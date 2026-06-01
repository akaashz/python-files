'''
0-100--->free--->600
100-300--->200*5--->1000---->400
300-500--->200*10--->2000---->200
200*15--->3500
500
'''

units=int(input("Enter the units consumed: "))
bill=0
if units<=100:
    bill=600        
elif units<=300:
    bill=600+(units-100)*5
elif units<=500:
    bill=600+200*5+(units-300)*10
else:
    bill=600+200*5+200*10+(units-500)*15
print("Electricity bill: ",bill)    
