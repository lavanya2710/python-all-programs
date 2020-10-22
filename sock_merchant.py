"""n=input()
socks = input()
pairs = 0

for element in set(socks):
	pairs += socks.count(element) // 2
print(pairs)

count=0
n = int(input())
c = [int (a) for a in input().strip().split(" ")]
c.sort()
for i in range(0,n-1):
    if c[i]==c[i+1]:
        c[i+1]=0
        count+=1
print(count)

count=0
n=int(input())
c=[int(a) for a in input().strip().split(" ")]
c.sort()
for i in range(0,n-1):
    if c[i]==c[i+1]:
        c[i+1]=0
        count+=1
print(count)"""

count=0
n = int(input())
c = [int(a) for a in input().strip().split(" ")]
c.sort()
for i in range(0,n-1):
    if c[i]==c[i+1]:
        c[i+1]=0
        count+=1
print(count)


count=0
n=int(input())
c=[int (a) for a in input().strip().split(" ")]
c.sort()
for i in range(0,n-1):
    if c[i]==c[i+1]:
        c[i+1]=0
        count=count+1
        print(count)

count=0
n=int(input())
c=[int (a) for a in input().strip().split()]
c.sort()
for i in range(0,n-1):
    if c[i]==c[i+1]:
        c[i+1]=0
        count=count+1
        print(count)
























