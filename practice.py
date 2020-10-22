"""#sock merchant
count=0
n=int(input())
c=[int(a) for a in input().strip().split(" ")]
c.sort()
for i in range(0,n-1):
    if c[i]==c[i+1]:
        c[i+1]=0
        count=count+1
print(count)

#counting valley
n=int(input())
s=input()
level=0
valley=0
for i in s:
    if i=="u":
        if level==-1:
            valley=valley+1
            level=level+1
    else:
        i=="d"
        level=level-1
print(valley)
#jumping clouds
n=int(input())
c=list(map(int,input().strip().split(" ")))
count=0
i=0
while(i<n-1):
    i=i+(c[i]==0)+1
    count=count+1
print(count)

#findingastring
n=int(input())
s=input()
c=s.count("a")
l=n//len(s)
i=n%len(s)
if i==0:
    c=c*l
else:
    c=c*l+s[:i].count("a")
print(c)

#leftrotation
def leftrotation(a,n,d):
    return a[d:]+a[:d]
n,d=map(int,input().strip().split(' '))
a=list(map(int,input().strip().split(' ')))
arr=leftrotation(a,n,d)
print(*arr,sep=" ")

#minimum swap of 2 elements
def swap(arr):
    a=[0]*(len(arr)+1)
    for val,pos in enumerate(arr):
        a[val]=pos
        pos=pos+1
        count=0
        for i in range(len(arr)):
            if arr[i]!=i+1:
                count=count+1
                t=arr[i]
                arr[a[i+1]]=t
                a[t]=i+1
        return swap

#2d array
def array(arr):
    sum=[]
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            sum.append(arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]) 
        return max(sum)

#new year chaos
def minimumbribes(q):
    bribes=0
    for i in range(len(q)-1,-1,-1):
        if q[i]-(i+1)>2:
            print("too chaotic")
            return
        for j in range(max(0,q[i]-2,i)):
            if q[j]>q[i]:
                bribes=bribes+1
            print(bribes)"""


