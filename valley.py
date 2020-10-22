"""n = int(input())
s = input()
valleys = 0
level = 0
for i in s:
    if i == 'U':
        if level == -1:
           valleys =valleys+1
        level =level+1
    elif i == 'D':
        level=level-1
print(valleys)

n=int(input())
s=input()
level=0
valleys=0
for i in s:
    if i=="u":
        if level==-1:
            valleys+=1
    level+=1
    elif i=="d":
            level-=1
print(valleys)"""


n=int(input())
s=input()
level=0
valley=0
for i in s:
    if i =="u":
        if level== -1:
            valley+=1
        level+=1
    elif i=="d":
        level-=1
print(valley)























































