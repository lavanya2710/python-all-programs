"""n=int(input())
c=list(map(int,input().strip().split()))
count=0
i=0
c.insert(n,0)
while(i<n-1):
    i+=(c[i+2]==0)+1
    count+=1
print(count)

n=int(input())
c=list(map(int,input().strip().split()))
count=0
i=0
c.insert(n,0)
while(i<n-1):
    i=i+ (c[i]==0)+1
    count=count+1
print(count)

n=int(input())
c=list(map(int,input().strip().split()))
count=0
i=0
c.insert(n,0)
while(i<n-1):
    i=i+ (c[i]==0)+1
    count=count+1
print(count)"""

n=int(input())
c=list(map(int,input().strip().split()))
count=0
i=0
while(i<n-1):
    i=i+(c[i]==0)+1
    count=count+1
print(count)

















