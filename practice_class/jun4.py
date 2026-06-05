# Reverse list

n=int(input())
lst=list(map(int,input().split()))[:n]

#res=[0]*n
#for i in range(n):
#   res[i]=lst[n-i-1]
#print(res)

start=0
end=n-1
while start<end:
    lst[start],lst[end]=lst[end],lst[start]
    start+=1
    end-=1
print(lst)

# Leetcode 268

lst=list(map(int,input().split()))
n=len(lst)
lst.sort()
for i in range(n):
    if i!=lst[i]:
        print(i)
        break
    else:
        print(n)
#print(n*(n+1)//2-sum(lst))

# Bubble Sorting

lst=list(map(int,input().split()))
n=len(lst)
for i in range(n-1):
    for j in range(n-i-1):
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1]=lst[j+1]+lst[j]
print(lst)

# Binary search
lst=list(map(int,input().split()))
n=len(lst)
target=int(input())
target=int(input())
low=0
high=n-1

while low<=high:
    mid=(low+high)//2
    if lst[mid]==target:
        print(mid)
        exit()
    elif target>lst[mid]:
        low=mid+1
    else:
        high==mid-1
        
print(-1)