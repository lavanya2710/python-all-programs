"""functions
it is a set of statements meant to do a particular task
def f():
    a=3
obj=f()
print
def f():
    a=3
    return a
obj=f()
print(obj)

#1> postion 
def f(name,age):
    print(name)
    print(age)
f("lavanya",23)
#2>keyword
def f(name,age):
    print(name)
    print(age)
f(age="lavanya",name=23)
#3>default
def f(name,age=24):
    print(name)
    print(age)
f("lavanya",23)
f("love")
#4> variable length argument
def f(name,*age):
    print(name)
    print(age)
f("lavanya",23,"bangalore",110095)
#5>keyword variable length argument
def f(name,**age):
    print(name)
    print(age)
f(name="lavanya",age=23,city="bangalore",pin=110095)

#global and local variable
a=5
def f():
    a=7
    print(a)
    global a
    a=6
    print(a)
f()
print(a)
#list of elements in functions
def count(list):
    even=0
    odd=0
    for i in list:
        if i%2==0:
            even=even+1
        else:
             odd=odd+1
    return even,odd
list=[1,2,3,4,5,6,7,8,9,10]
e,o=count(list)
print(e)
print(o)
#fibonacci
def fib(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)
fib(10)
#factorial
def fac(x):
    f=1
    for i in range(1,x+1):
        f=f*i
    return f
n=5
result=fac(n)
print(result)
#prime or not
#divide by 1 or itself
num=14
for i in range(2,num):
    if num%i==0:
        print("not prime")
        break
    else:
        print("prime")
        break
from functools import reduce
a=[1,2,3,4,5,6]
result=list(filter(lambda n:n%2==0,a))
print(result)
 
result1=list(map(lambda n:n*2,a))
print(result1)

result2=reduce(lambda m,n:m+n,a)
print(result2)
#decorators
def div(a,b):
    if a<b:
        a,b=b,a
    print(a/b)
div(3,6)

def div(a,b):
    print(a/b)
    def smart_div(func):
        def inner(a,b):
            if a<b:
                a,b=b,a
            return func(a,b)
        return inner
div1=smart_div(div)
div(2,4)
class it is a design or blueprint of an object
object- it is an entity having attribute and behaviour
attributes=vriables
behaviour=methods(same as functions)
#class
class a:#class
    def b(self):#method
        print("hello")
        print("world")
obj=a()#object creation
obj.b()
#constructor it represents an object the task is to initialize the value to the data member of the class and obect of class is created
class a:
    def __init__(self):
        print("hello")
    def b(self):
        print("world")
obj=a()
obj.b()
#polymorphism
#3types operator overloading,method overloading,method overriding
#operator overloading
class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self,other):
        a1=self.a+other.a
        b1=self.b+other.b
        obj2=A(a1+b1)
obj=A(5,6)
obj1=A(7,8)
obj2=obj.__add__(obj1)
print(obj.a,obj.b)
print(obj1.a,obj1.b)
#method overloading- python will not support method overloading
#operator overriding
class student:
    def b(self):
        print("hi")
    def b(self):
        print("hello")
    def b(self):
        print("world")#overriding
obj=student()
obj.b()
#inheritance -inheriting the data from super class to sub class 
#single
class a:
    def f1(self):
        print("hi")
    def f2(self):
        print("hiiii")
class b(a):
    def f3(self):
        print("hello")
    def f4(self):
        print("hellllloooo")
class c(b):
    def f5(self):
        print("world")
    def f6(self):
        print("worlddddddd")

obj=b()
obj.f2()
#multilevel
#multiple
#data abstraction-the process of hiding the real implementation from the application user.for acheiving data there are 2 things abstract classes and abstract methods
#abstract class =it means classes which are made up of abstract method
#abstract method-which is having declaration but no defination and cant create object.
class abstract:
    def b(self):
        pass
#encapsulation=binding the data into a single unit we have to use private method__
class a:
    __d=3
    __e=7
    def b(self):
        print("hi",self.__e)
    def c(self):
        print(self.__d)
obj=a()
obj.b()
obj.c()

#types of variables-2 instance variable,class(static)variable
class student:
    school="lpu"
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def b(self):
        print("hi",self.m1,self.m2)

obj=student(50,60)
obj.school()
obj.m1=70#instance
obj.b()
#time complexity O(n)
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
m=factorial(5)
print(m)
#time complexity 
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
m=fib(11)
print(m)
#selection sorting
list=[1,4,5,6,3,2,7,0,9]
for i in range(len(list)):
    min_val=max(list[i:])
    min_index=list.index(min_val)
    list[i],list[min_index]=list[min_index],list[i]
print(list)
#bubble sort
list=[1,4,5,6,3,2,7,0,9]
flag=0
for j in range(len(list)-1):
    for i in range(len(list)-1):
        if list[i]>list[i+1]:
            list[i],list[i+1]=list[i+1],list[i]
            flag=1
            if flag==0:
                break
print(list)
#insertion sort
def insertion(list):
    for i in range(1,len(list)):
        cur=list[i]
        pos=i
        while cur>list[pos-1] and pos>0:
            list[pos]=list[pos-1]
            pos=pos-1
            list[pos]=cur
list=[1,4,5,6,3,2,7,0,9]
insertion(list)
print(list)
#merge sort
def merge(list):
    if len(list)>1:
        mid=len(list)//2
        l=list[:mid]
        r=list[mid:]
        merge(l)
        merge(r)
        i=j=k=0
        while i<len(l) and j<len(r):
            if l[i]<r[j]:
                list[k]=l[i]
                i=i+1
            else:
                list[k]=r[j]
                j=j+1
            k=k+1
        while i<len(l):
            list[k]=l[i]
            i=i+1
            k=k+1
        while j<len(r):
            list[k]=r[j]
            j=j+1
            k=k+1
def printlist(list):
    for i in range(len(list)):
        print(list[i])
    print()
list=[1,4,5,6,3,2,7,0,9]
merge(list)
print(list)

s="abcac"
n=7
m=len(s)
l=n/m
print(l)
q=s*l
print(q)
print(q.count("a"))
#leftrotation
def leftrotation(arr,d,n):
    for i in range(d):
        leftrotationbyone(arr,n)
def leftrotationbyone(arr,n):
    temp=arr[0]
    for i in range(n-1):
        arr[i]=arr[i+1]
    arr[n-1]=temp
def printarray(arr,size):
    for i in range(size):
        print(arr[i])
arr=[1,2,3,4,5]
leftrotation(arr,2,5)
printarray(arr,5)
#
a=[1,2,3,4,5,6,7,8,9,10]
for i in range(len(a)-1,-1,-1):
    if a[i]-(i+1)>2:
        print("too chaotic")
    for j in range(max(0, a[i] - 2),i):
        if a[j]>a[i]:
            bribes+=1
        print(bribes)
arr=[1,3,5,2,4,6,7]
def minimumSwaps(arr):
    a=[0]*(len(arr)+1)
    for val,pos in enumerate(arr):
        a[val]=pos
        pos=pos+1
    for i in range(len(arr)):
        if arr[i]!=i+1:
            count=0
            t=arr[i]
            arr[a[i+1]]=t
            a[t]=i+1
            return minimumSwaps
        min_val=min(arr[i:])
        min_index=arr.index(min_val)
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr
#bubble sort
arr=[5,3,2,4,1]
swap=0
for j in range(len(arr)-1):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
            swap+=1
print(swap)
print(arr[-1])
print(arr)

#merge sort
def merge(arr):
    if len(arr)>1:
        mid=len(arr)//2
        l=arr[:mid]
        r=arr[mid:]
        merge(l)
        merge(r)
        i=j=k=0
        swap=0
        count=0
        while i<len(l) and j<len(r):
            if l[i]<r[j]:
                arr[k]=l[i]
                i=i+1
            else:
                arr[k]=r[j]
                j=j+1
            k=k+1
        while i<len(l):
            arr[k]=l[i]
            i=i+1
            k=k+1
        while j<len(r):
            arr[k]=r[j]
            j=j+1
            k=k+1
            if arr is sorted:
                return 0
            else:
                swap+=1
            
def printarray(arr):
    for i in range(len(arr)):
        print(arr[i])
#main
arr=[2,3,4,2,3,6,8,4,5]
merge(arr)
printarray(arr)1

def linearsearch(list,key):
    list1=[]
    flag=0
    for i in range(len(list)):
        if key==list[i]:
            flag=True
            list1.append(i)
    if flag==True:
        print("key found")
        for i in list1:
            print(i)
    else:
        print("not found")
list=[5,99,34,2,54,65]
key=34
linearsearch(list,key)
#binary search
def binary(list,key):
    low=0
    high=len(list)-1
    
    flag=False
    while low<=high and not flag:
        mid=(low+high)//2
        if key==list[mid]:
            flag=True
        elif key>=list[mid]:
            low=mid+1
        else:
            high=mid-1
    if flag==True:
        print("key found")
    else:
        print("not found")
list=["helo","hi","hello"]
list.sort()
key="hell"
binary(list,key)
def whatFlavors(cost, money):
    remains = dict()
    for index, c in enumerate(cost):
        if c not in remains:
            remains[money - c] = index + 1
        else:
            print(remains[c], index + 1)


#prime
n=10
for i in range(2,n):
    if i%n==0:
        print("prime")
        break
    else:
        print("not prime")
        break
#fabinoci
def fib(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)
fib(15)  
#factorial
def fact(x):
    f=1
    for i in range(1,x+1):
        f=f*i
    return f
n=4
result=fact(n)
print(result)
#recursion
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
result=fact(4)
print(result)
#recursion fib
def fib(n):
    if n<=0:
        print("incorrect input")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(9))"""
#left rotation
def leftrotation(arr,d,n):
    for i in range(d):
        leftrotationbyone(arr,n)
def leftrotationbyone(arr,n):
    temp=arr[0]
    for i in range(n-1):
        arr[i]=arr[i+1]
    arr[n-1]=temp
def printarray(arr,size):
    for i in range(size):
        print(arr[i])
arr=[1,2,3,4,5]
leftrotation(arr,2,5)
printarray(arr,5)
