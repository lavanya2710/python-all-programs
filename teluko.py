"""a=[1,2,3,4,5,]
b=["lav","pav","bav"]
c=[a,b]
print(c)
a.append(8)
print(a)
a.insert(2,10)
print(a)
a.remove(5)
print(a)
b.remove("bav")
print(b)
a.pop(0)
print(a)
a.pop()
print(a)
del a[3:]
print(a)
a.extend([1,2,3,4])
print(a)
print(min(a))
print(max(a))
print(sum(a))
print(len(a))
a.sort()
print(a)
print(sum(a))
tup=(1,32,3,4,4,5,8)
print(tup[0])
print(tup[2:])
print(tup.count(4))
set={1,3,4,4,5,8,4,3,2,6,4,5,6,3,6,6,43,2,2,3}
print(set)
set.remove(5)
print(set)
a=5
b=a
print(id(a))
print(id(b))
k=1
print(id(k))
a=8
print(id(a))
a1=8.0
print(type(a1))
a2=8
print(type(a2))
a3="8"
print(type(a3))
a4="c"
print(type(a4))
a5="lavanya"
print(type(a5))
a=5.6
b=int(a)
print(type(b))
a=5
b=float(a)
print(type(b))
a=5
b=str(a)
print(type(b))
a=9
b=8
c=complex(a,b)
print(c)
a=9
b=8
c=bool(a<b)
print(c)
a=int(True)
print(a)
list=[1,2,3,4,0,6,9]
print(type(list))
print(list(range(10)))
dict={"iphone":"vla","mi":"lav","samsung":"nya"}
a=dict.keys()
b=dict.values()
print(a)
print(b)
print(dict["iphone"])
print(dict.get("samsung"))
a=9
b=3
print(a+b)
print(a-b)
print(a*b) 
print(a/b)
print(a//b)
print(a**b)
print(a%b)
x=2
x+=2
print(x)
x-=2
print(x)
a,b=5,6
print(a,b)
a=7
print(a)
a=-a
print(a)
a=8
b=9
print(a>b)
print(a<b)
print(a==b)
a=True
print(not(a))
a=25
print(bin(a))
print(oct(a))
print(hex(a))
a=45
print(~a)
import math as m
a=5
print(math.sqrt(a))
print(math.ceil(a))
print(math.floor(a))
print(math.pow(a,2))
print(math.pi)
print(m.ceil(a))

from math import sqrt,pow
print(sqrt(5))
a=int(input())
b=int(input())
c=a+b
print(c)
a=input()[1:]
print(a)
result=eval(input("enter a exp"))
print(result)

import sys
a=sys.argv[0]
b=sys.argv[0]
c=a+b
print(c)

if False:
    print("hi")
print("bye")

x=3
r=x%2
if r==0:
    print("even")

print("bye")

x=3
r=x%2
if r==0:
    print("even")
if r==1:
    print("odd")

x=3
r=x%2
if r==0:
    print("even")
else:
    print("odd")
x=8
r=x%2
if r==0:
    print("even")
    if x>5:
        print("great")
if r==1:
    print("odd")
x=5
if x==1:
    print("one")
elif x==2:
    print("two")
else:
    print("invalid")

i=1
while i<=5:
    print("hello")
    i=i+1

i=1
while i<=1:
    print("hello")
    j=1
    while j<=4:
        print("world")
        j=j+1
    i=i+1
a=["lav",55,9.2]
for i in a:
    print(i)
a=("lavanya")
for i in a:
    print(i)
a={1,2,3,34,5,6,6,6}
for i in a:
    print(i)
for i in range(10):
    print(i)
for i in range(1,50,5):
    print(i)
for i in range(20,1,-1):
    print(i)
for i in range(0,21):
    if i%5==0:
        print("divisible")
        print(i)
available=5
x=int(input("enter candy"))
i=1
while i<=x:
    if i>available:
        print("out of stock")
        break
    print("candy")
    i=i+1
print("bye")

for i in range(0,20):
    if i%3==1 or i%5==1 :
        continue
    print(i)
       
for i in range(0,100):
    if i%2==0:
        pass
    else:
        print(i)
for i in range(4):
    for j in range(4):
        print("*",end="")
print()     

for i in range(0,4):
    for j in range(4-i):
        print("#",end="")
        i=i+1
class a:
    def __init__(self,a,b): 
        self.a=a
        self.b=b
    def bi(self):
        print(55,self.a,self.b) 
obj=a(52,12)
obj.bi()   

class a:
    def __init__(self):
        self.name="lav"
        self.age=23

obj=a()
obj.name="love"
print(obj.name)
print(obj.age)

class a:
    def __init__(self):
        self.name="lav"
        self.age=23
    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False

obj=a()
obj1=a()
obj1.age=30
if obj.compare(obj1):
    print("same")
else:
    print("different")
print(obj.name)
print(obj.age)
print(obj1.name)
print(obj1.age)

class a:
    wheel=4
    def __init__(self):
        self.mil=10
        self.com="bmw"

obj=a()
obj1=a()
a.wheel=5
obj.mil=9
print(obj.mil,obj.com,obj.wheel)
print(obj1.mil,obj1.com,obj.wheel)
#instance methods
class student:
    school="lpu"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    def get_m1(self):
        return self.m1
    def set_m1(self,values):
        self.m1=values

obj=student(22,93,24)
obj1=student(21,52,23)
print(student.school)
print(obj.avg())
print(obj1.avg())
print(obj.m1,obj.m2,obj.m3)
print(obj1.m1,obj1.m2,obj1.m3)
print(obj.get_m1())
print(obj.m1,obj.m2,obj.m3)
print(obj1.set_m1(12))
print(obj1.m1,obj1.m2,obj1.m3)

#class method
class student:
    school="lpu"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    @classmethod
    def info(cls):
        return cls.school
obj=student(22,93,24)
obj1=student(21,52,23)
print(student.school)
print(obj.m1,obj.m2,obj.m3)
print(obj1.m1,obj1.m2,obj1.m3)
print(student.info())
#static method
class student:
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    @staticmethod
    def info():
        print("hi")
obj=student(1,2,3)
obj1=student(2,3,4)
student.info()
#inner class
class student:

    def __init__(self,name,rollno):
        self.name= name
        self.rollno= rollno
        self.lap= self.laptop()
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()
    class laptop:
        def __init__(self):
            self.brand="hp"
            self.cpu="i5"
        def show(self):
            print(self.brand,self.cpu)
                
s1=student("lav",10)
s2=student("love",1)
s1.show()
s2.show()
####s1.lap.brand
lap1=s1.lap
lap2=s2.lap
print(id(lap1))
print(id(lap2))
lap1=student.laptop()####
s1.show()
s2.show()
#inheritance
#(simple program)
class a:
    def feature1(self):
        print("feature1 is working")
    def feature2(self):
        print("feature2 is working")
class b:
    def feature3(self):
        print("feature3 is working")
    def feature4(self):
        print("feature4 is working")
a1=a()
b1=b()
a1.feature1()
a1.feature2()
b1.feature2()#showing error so thats why we use inheritance
b1.feature4()
#single inheritance
class a:
    def feature1(self):
        print("feature1 is working")
    def feature2(self):
        print("feature2 is working")
class b(a):
    def feature3(self):
        print("feature3 is working")
    def feature4(self):
        print("feature4 is working")
a1=a()
b1=b()
a1.feature1()
a1.feature2()
b1.feature2()
b1.feature4()

#multi level
class a:
    def feature1(self):
        print("feature1 is working")
    def feature2(self):
        print("feature2 is working")
class b(a):
    def feature3(self):
        print("feature3 is working")
    def feature4(self):
        print("feature4 is working")
class c(b):
    def feature5(self):
        print("feature5 is working")
    def feature6(self):
        print("feature6 is working")
a1=a()
b1=b()
c1=c()
a1.feature1()
a1.feature2()
b1.feature2()
b1.feature4()
c1.feature4()
c1.feature1()

#multiple
class a:
    def feature1(self):
        print("feature1 is working")
    def feature2(self):
        print("feature2 is working")
class b:
    def feature3(self):
        print("feature3 is working")
    def feature4(self):
        print("feature4 is working")
class c(a,b):
    def feature5(self):
        print("feature5 is working")
    def feature6(self):
        print("feature6 is working")
a1=a()
b1=b()
c1=c()
a1.feature1()
a1.feature2()
b1.feature3()
b1.feature4()
c1.feature1()
c1.feature6()
#constructor
class a:
    def __init__(self):
        print("hello")

    def feature1(self):
        print("feature1 is working")
    def feature2(self):
        print("feature2 is working")
class b(a):
    def __init__(self):
        print("hello world")

    def feature3(self):
        print("feature3 is working")
    def feature4(self):
        print("feature4 is working")

a1=b()
#super keyword

class a:
    def __init__(self):
        print("hello")
    def feature1(self):
        print("feature1 is working")
    def feature2(self):
        print("feature2 is working")
class b(a):
    def __init__(self):
        super().__init__()
        print("hello world")
        
    def feature3(self):
        print("feature3 is working")
    def feature4(self):
        print("feature4 is working")
a1=b()

#
class a:
    def __init__(self):
        print("hello")
    def feature1(self):
        print("feature1 is working")
    def feature2(self):
        print("feature2 is working")
class b:
    def __init__(self):
        print("hello world")
        
    def feature1(self):
        print("feature3 is working")
    def feature2(self):
        print("feature4 is working")
class c:
    def __init__(self):
       # super().__init__()
        print("hello c")
    def feat(self):
        super().feature2()
a1=c()
a1.feat()

class visual:
    def excute(self):
        print("running")
        print("compiling")
class myeditor:
        def excute(self):
            print("best")
            print("running")
            print("compiling")
class laptop:
        def code(self,ide):
            ide.excute()
a=myeditor()
obj=laptop()
obj.code(a)
#operator overloading
a="5"
b="6"
print(str.__add__(a,b))

class student:
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        m3=self.m3+other.m3
        obj2=student(m1,m2,m3)
        return obj2

obj=student(11,22,33)
obj1=student(1,2,33)
obj2 =obj1 + obj
print(obj2.m2)

class student:
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def __sub__(self,other):
        m1=self.m1-other.m1
        m2=self.m2-other.m2
        m3=self.m3-other.m3
        obj2=student(m1,m2,m3)
        return obj2

obj=student(11,22,33)
obj1=student(1,2,33)
obj2 =obj1 - obj
print(obj2.m2)

class student:
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        m3=self.m3+other.m3
        obj2=student(m1,m2,m3)
        return obj2
    def __gt__(self,other):
        r1=self.m1+self.m2+self.m3
        r2=other.m1+other.m2+other.m3
        if r1>r2:
            return True
        else:
            return False
    def __str__(self):
        return "{} {} {}".format(self.m1,self.m2,self.m3)
obj=student(11,22,33)
obj1=student(1,1000,33)
if obj>obj1:
    print("yes")
else:
    print("no")

a=5
print(a.__str__())
print(obj)

class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def sum(self,a,b,c):
        s=a+b+c
        return s
s1=student(4,5)
print(s1.sum(1,5,9))

class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def diff(self,a,b):
        s=a-b
        return s
s1=student(4,5)
print(s1.diff(1,5))

class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def sum(self,a=None,b=None,c=None):
        s=0
        if a!=0 and b!=0 and c!=0:
            s=a+b+c
        elif a!=0 and b!=0:
            s=a+b
        else:
            s=a
        return s
s1=student(4,5)
print(s1.sum(1,2))

class a:
    def show(self):
        print("hi")
class b(a):
    def show(self):
        print("world")
a1=b()
a1.show()
#exceptional handling

a=5
b=2
try:
    print(a/b)
except Exception:
    print("uh cannot divide num by 0")
print("bye")

a=5
b=0
try:
    print(a/b)
except Exception as e:
    print("uh cannot divide num by 0",e)
print("bye")
a=5
b=2
try:
    print("resource open")
    print(a/b)
    
except Exception:
    print("uh cannot divide num by 0")
finally:    
    print("resource closed")
print("bye")

a=5
b=4

try:
    print("resource open")
    print(a/b)
    k=int(input("enter a num"))
    print(k)

except ZeroDivisionError as e:
    print("uh cannot divide num by 0",e)
except ValueError as e:
    print("invalid input")
except Exception as e:
    print("something went wrong")
finally:    
    print("resource closed")
print("bye")

#multithreading
from time import sleep
from threading import *
class hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
            sleep(i)

class hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")

a1=hello()
a2=hi()
a1.start()
sleep(0.2)
a2.start()
a1.join()
a2.join()
print("byee")
#file handling
f=open("lavanya","r")
print(f.readline)
print(f.readline(4),end="")
f=open("lavanya","a")
f.write("hello lavanya how are uh")
f.write("lavanya")
#linear search
pos=-1
def search(list,n):
    i=0
    while i<len(list):
        if list[i]==n:
            globals()['pos']=i
            return True
        i=i+1
    return False

list=[5,8,4,6,9,2]
n=9
if search(list,n):
    print("found",pos)
else:
    print("not found")
pos=-1
def search(list,n):
    i=0
    for i in range(len(list)):
        if  i<len(list)==n:
            globals()["pos"]=i
            return True
    return False

list=[5,8,4,6,9,2]
n=9
if search(list,n):
    print("found",pos)
else:
    print("not found")

#prime or not
num=10
for i in range(2,num):
    if num%i==0:
        print("not prime")
        break
    else:
        print("prime")
num=int(input("enter a val"))
for i in range(2,num):
    if num%i==0:
        print("not prime")
        break
else:
    print("prime")
#array
from array import *
val=array("i",[1,2,3,5,4,-55,6])
val.reverse()
print(val[0:2])

from array import *
val=array("i",[1,2,3,5,4,-55,6])
for i in val:
    print(i)

from array import *
val=array("i",[1,2,3,5,4,55,6])
#newarr= array(val.typecode,(a for a in val))
newarr= array(val.typecode,(a*a for a in val))
for i in newarr:
    print(i)

from array import *
val=array("i",[1,2,3,5,4,55,6])
#newarr= array(val.typecode,(a for a in val))
newarr= array(val.typecode,(a*a for a in val))
i=0
while i<len(newarr):
    print(newarr[i])
    i+=1

from array import *
arr=array('i',[])
n=int(input("enter a length"))
for i in range(n):
    x=int(input("enter a array"))
    arr.append(x)

print(arr)

val=int(input("enter a value for search"))
k=0
for e in arr:
    if e==val:
        print(k)
        break
    k=k+1  

#function
def greet():
    print("hi")
    print("hello")
greet()
greet()

def add_sub(a,b):
    c=a+b
    d=a-b
    return c,d

result1,result2=add_sub(5,4)
print(result1,result2)

def add(a,b):
    c=a+b
    return c
d=add(4,5)
print(d)

def update(x):
    print(id(x))
    x=8
    print(x)

a=11
print(id(a))
update(a)
print(a)
#mutable
def update(x):
    x[1]=9
    print(x)
x=[1,2,3,4,6,7,5]
update(x)
def sum(a,b):
    c=a+b
    print(c)
sum(1,5)
def person(name,age):
    print(name)
    print(age)
person(age=24,name="lava")

def person(name,age=18):
    print(name)
    print(age)
person("lav",24)

def sum(a,b,c,d,e,f):
    g=a+b+c+d+e+f
    print(g)
sum(1,5,5,1,7,9)

def sum(a,*b):
    c=a
    for i in b:
        c=c+i
    print(c)
sum(5,6,34,78)

def sum(*b):
    c=0
    for i in b:
        c=c+i
    print(c)
sum("a","b","c","d")

def person(name,**data):
    print(name)
    print(data)
person(name="lava",age=23,city="bang",num=836029)
def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)
person(name="lava",age=23,city="bang",num=836029)
#global&local variable
a=10

def some():
    a=9
    print(a)
    global a
    a=15
    print(a)
some()
print(a)

#list in a function
def count(list):
    even=0
    odd=0
    for i in list:
        if i%2==0:
            even=even+1
        else:
            odd=odd+1
    return even,odd
list=[1,5545,456,546,549656,4847,4848,8787,999]
even,odd=count(list)
print(even)
print(odd)

def count(list):
    a=0
    b=0
    for i in range (len(list)):
        if len(list[i]) >=5 :
            a=a+1
        else:
            b=b+1
    return a,b
list=["lavanya","rakhi","ritu","lav","love","binduuuu","deepikaaaa"]
a,b=count(list)
print("names len more than 5",a)
print("less than 5",b)
#fibnocii
def fib(n):
    a=0
    b=1
    if n<=0:
        print("invalid")
    elif n==1:
        print(a)
    else:
        print(a)
        print(b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)

fib(10)

def fib(n):
    a=0
    b=1
    if n<=0:
        print("invalid")
    elif n==1:
        print(a)
    else:
        print(a)
        print(b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)
        if c>n:
            print(c)
            break
fib(100)
#factorial
def fac(x):
    f=1
    for i in range(1,x+1):
        f=f*i
    return f
n=4
result=fac(n)
print(result)

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
result=fact(5)
print(result)

#lambda
f=lambda a:a*a
result=f(5)
print(result)

def is_even(n):
    return n%2==0
num=[1,2,3,5,5,66,7,9]
even=list(filter(is_even,num))
print(even)

def is_odd(n):
    return n%2!=0
num=[1,2,3,5,5,66,7,9]
odd=list(filter(is_odd,num))
print(odd)

f=lambda num:num%2==0
num=[1,2,3,5,5,66,7,9]
even=list(filter(f,num))
print(even)

f=lambda num:num%2!=0
num=[1,2,3,5,5,66,7,9]
odd=list(filter(f,num))
print(odd)

#bubble sorting
def sort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp

arr=[9,5,7,6,1,2,4]
sort(arr)
print(arr)"""





