str=input()
str=str.capitalize()
print(str)

str=input()
print(str.count("i"))

#endswith
str=input()
print(str.endswith('o'))

str=input()
print(str.index('H'))

str=input()
print(str.isalnum())

#lowercase
str=input()
print(str.islower())

#uppercase
str=input()
print(str.isupper())

str=input()
print(str.swapcase())

#
str=input()
res=""
for i in str:
    if i>='A':
        if i>='A' and i<='Z':
            res+=chr(ord(i)+32)
        else:
            res+=chr(ord(i)-32)
print(res)

str=input()
arr=str.split()
print(str)
print(" ".join(str))

#Replace
str=input()
str.replace("l","A")
print(str)

#
str=input()
print(str.startswith('H'))

#
str=input()
arr=list(str)
print(arr)

start=0
end=len(str)

while start<end:
    arr[start],arr[end] =arr[end],arr[start]
    start+=1
    end-=1
    
print("".join(arr))

#palindrome check
str=input()
arr=list(str)
print(arr)

start=0
end=len(str)

while start<end:
    arr[start],arr[end] =arr[end],arr[start]
    start+=1
    end-=1
    
print("".join(arr))
    # OR
#rev="".join(arr)
#print(str==rev) 

str=input()
ch=input()[0]
first=last=-1

for i in range(len(str)):
    if str[i]==chr:
        if first==-1:
            first=i
        last=i
        
print(first,last)

#count the no of votes and print the number of votes

