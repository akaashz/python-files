
#star printing or pattern 

n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end="")
    print()
    
#gap between stars

n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print("*",end="")
        else:
            print(" ",end="")
    print()
 
 #i==j for print diagonal star
    
    n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n or i==j:
            print("*",end="")
        else:
            print(" ",end="")
    print()
        
# N+1 condition for diagonal from right to left       
        
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n or i==j or i+j==n+1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    
#triangle star pattern

n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i>=j:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    
#right angle triangle

n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j<=n+1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    
#left angle triangle
    
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j>=n+1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    
#Pyramid star pattern
    
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j>=n+1 and i<=j:
            print("*",end="")
        else:
            print(" ",end="")
    print()
 
#reverse pyramid star pattern    
    
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i<=j:
            print("*",end="")
        else:
            #remove the space between stars to get reverse pyramid
            print(" ",end="")
    print()
    
    
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j>=n+1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
for i in range(2,n+1):
    for j in range(1,n+1):
        if i<=j:
            print("*",end="")
        else:
            print(" ",end="")
    print()    

#hourglass star pattern

n = int(input())

# Upper half
for i in range(1, n + 1):
    for j in range(1, 2 * n):
        if j >= i and j <= (2 * n - i):
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Lower half
for i in range(n - 1, 0, -1):
    for j in range(1, 2 * n):
        if j >= i and j <= (2 * n - i):
            print("*", end="")
        else:
            print(" ", end="")
    print()
    
#odd number pyramid star pattern

n=int(input())
for i in range(1,n+1):
    for j in range(1,2*n):
        if j>=n+1-i and j<=n-1+i:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    
#Pattern sums from drive:

#1)
n=int(input())
for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    print() 

#2 
n=int(input())
for i in range(1,n+1):
    for j in range(n-i):
        print("*",end="")
    print() 
    
#3
n=int(input())
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    
    for j in range(i):
        print("* ", end="")
    
    print()
    
#4
n=int(input())
for i in range(1, n + 1):
    for j in range(n-i):
        print(" ", end="")
    
    for k in range(1,i*2):
        if k==1 or k==2*i-1 or i==n:
            print("*", end="")
        else:
            print(" ", end="")  
   
    print()
    
#5
n=int(input())