
# LIST

l=list(range(5,10+1,2))

n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
print(l)

l=list(map(int,input().split()))

#list comprehension
l=[int(x) for x in input().split()]

#to find length of list
l=[10,20,30,40,50]
print(len(l))

#count
l=[10,20,30,40,50,10,10]
print(l.count(10))

##to insert using append
l=[20,30,40,50,10,10]
l.append(100)
l.append(120)

print(l)

#extend

l=[20,30,40,50,10,10]
l1=[100,200,300]
l1.extend(l1)
print(l)

#pop
l=[10,20,30,40,50]
l.pop()
l.pop(2)
print(l)

# Clear function
l=[10,20,30,40,50]
l.clear()
print(l)

#to delete the object
l=[10,20,30,40,50]
del l
print(l) #error

#copy
l1=l.copy()
print(l1)

#reverse
l=[10,20,30,40,50]
l.reverse()
print(l)

#sort
l=[50,40,30,20,10]
l.sort()
print(l)
l.sort(reverse=True)
print(l)

#To find the min,max,sum
l=[10,20,30,40,50]
print(min(l))
print(max(l))
print(sum(l))

#To print the values in the list
lst=[]
for i in range(n):
    lst.append(int(input()))
for i in lst:
    print(i,end=" ")

#To print the sum of values in the list
sum=0
for i in lst:
    sum+=i
print(sum)

#list mapping

n=int(input())
lst=list(map(int,input().split()))[:n]
print(lst)

#To find the maximum element in the list
n=int(input())
lst=list(map(int,input().split()))[:n]
max=lst[0]

for i in range(1,n):
    if lst[i]>max:
        max=lst[i]        
print(max) 


#283 leetcode and to move the zeroes to the end of the list
n=int(input())
lst=list(map(int,input().split()))[:n]
ind=0
for i in range(n):
    if lst[i]!=0:
        lst[ind]=lst[i]
        ind+=1
for i in range(ind,n):
    lst[ind]=0
for i in lst:
    print(i,end=" ")
    
#to swap the non zero elements with the zero elements    
n=int(input())
lst=list(map(int,input().split()))[:n]
ind=0
for i in range(n):
    if lst[i]!=0:
        lst[ind],lst[i]=lst[i],lst[ind]
        ind+=1

for i in lst:
    print(i,end=" ")

#Searching an element in the list
n=int(input())
lst=list(map(int,input().split()))[:n]
target=int(input())
for i in lst:
    if i==target:
        print(lst.index(i))
        break
    else:
        print(-1)  
        
#To write a program to reverse the list without using new list
       

    