"""#1
def countswap(a):
    swap=0
    for j in range(len(a)-1):
        for i in range(len(a)-1):
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
                swap=swap+1
    print("Array is sorted in %s swaps." %swap)
    print("First Element:",a[0])
    print("Last Element:",a[-1])
n=int(input(""))
a=list(map(int,input().split()))
countswap(a)
#2
def maximumToys(prices, k):
    count=0
    total=0
    prices.sort()
    for i in prices:
        total=total+i
        if total<=k:
            count=count+1
    return count
 #3
class player:
    def __init__(self,name,score):
         self.name=name
         self.score=score
    def __comparator__(a,b):
        if score.a<score.b:
            return 1
        elif score.a==score.b:
            if a.name<b.name:
                return 1
            else:
                return -1
        else:
            return -1"""

#4
"""def bank(exp,d):
    d=5
    for i in range(d[0],d[2]):
       print(i)
    exp=[2,3,4,2,3]
    exp.sort()
    print(exp)
    n=len(exp)
    median=n/2
    median1=n+1/2
    #for i in exp:
    #for j in range():
        #print(i)
    if n%2==0:
        return median
    else:
        return median1
obj=bank([2,3,4,2,3],5)
print(obj)

meal_cost=float(input(""))
tip_percent=int(input(""))
tax_percent=int(input(""))
tip=meal_cost*tip_percent/100
tax=(meal_cost*tax_percent)/100
total_cost=meal_cost+tip+tax
print(round(total_cost))

n=int(input("enter"))
if n%2==1:
    print("weird")
elif n%2==0 and n in range(2,6):
    print("not weird")
elif n%2==0 and n in range(6,21):
    print("weird")
elif n%2==0 and n>20:
    print("not weird")

class Person:
    def __init__(self,initialAge=0):
        self.initialAge=age
        if initialAge<0:
            print("Age is not valid, setting age to 0.")
    def amIOld(self):
        if age<13:
            print("You are young.")
        elif 18<age>13:
            print("You are a teenager.")
        else:
            print("You are old.s")
    def yearPasses(self):
        self.initialAge=age
        age=age+1
        return 

t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")


class MyQueue(object):
    def __init__(self):
        self.mouth = []
        self.butt = []
    
    def peek(self):
        self.digest()
        return self.butt[-1]
        
    def pop(self):
        self.digest()
        return self.butt.pop()
        
    def put(self, value):
        self.mouth.append(value)
        
    def digest(self):
        if len(self.butt) == 0:
            while len(self.mouth) > 0:
                self.butt.append(self.mouth.pop())


n=2
for i in range(1,11):
    result=n*i
    print(n"x"i'=',result)

n=3
a=[67,68,69]
b=[70,98,63]
c=[52,56,60]
average=a[0]+a[1]+a[2]/3
print(average)"""

a=("this is a string")
print(a.split())
a="-".join(a)
print(a)