#in bank to find how many digits are present in the account number

n=int(input("Enter account number : "))
count=0
while n>0:
    n=n//10
    count=count+1   
print(count)    


