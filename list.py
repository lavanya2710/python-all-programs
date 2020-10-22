"""a=[]
a.append(1)
a.append('apple')
print(a)"""

"""a=input("enter a name")
print("hello",a)"""

"""a=int(input("enter 1num"))
b=int(input("enter 2num"))
c=a+b
print(c)"""

"""a=10
if a<20:
    print("a is bad")
elif a>10:
    print("a is good")
else:
    print("a is great")"""


"""def a(): 
    print("hello")
    print("hello again")
a()"""

"""def getinteger():
    result = int(input("enter a num"))
    return result
def b():
    print("started")
    output = getinteger()
    print(output)
if __name__=="__main__":
    b()"""

"""for a in range(5):
    print(a)

for b in range(10):
    print(b)"""

"""import math
def b():
    num=float(input("enter a value"))
    num=math.fabs(num)
    print(num)
if __name__=="__main__":
    b()"""

"""print("my name\nis lavanya")"""

"""print(r"my name\n")"""

"""i=3
print(i)
i=i+1
print(i)
s='''this is book
written by swaroop'''
print(s)"""

"""i=5
print(i)"""

"""i=1;
print(i);"""

"""s='this is\
    lavanya'
print(s)"""

"""a=[1,2,3]
b=[4,5,6]
print(a)
print(b)"""

"""a=2
a=3*a
print(a)"""

"""a=2
a*=3
print(a)"""

"""a=3+2
print(a)

a=3-2
print(a)

a=3*2
print(a)

a=2
b=4
c=a**b
print(c)

a=10
b=2
c=a/b
print(c)

a=19
b=2
c=a//b
print(c)

a=11
b=2
c=a%b
print(c)

a=2
b=2
c=a<<b
print(c)

a=11
b=1
c=a>>b
print(c)


x=int(input("enter a value"))
x1=x+1
print(x1)

a=3+2*2
print(a)

a=((2+2)*3)
print(a)

list=[]
print(list)

a=[1,2,3,4]
print(a)
print(a[2])

list=["geeks","for","geeks"]
print(list)
print(list[2])
print(list[1])

a=[["hello","world"],["how","are","you"]]
print(a)

a=[1,2,3,4]
print(len(a))
a.append(3)
print(a)

a=[1,2,3]
for i in range(1,4):
    a.append(i)
print(a)

a=[1,2,3]
a.append((8,7))
print(a)
a=[1,2,3]
b=[5,6,7]
a.append(b)
print(a)

a=[1,2,3]
a.insert(4,6)
a.insert(0,9)
print(a)

a=[1,2,3]
a.extend(["geeks","a",0.9])
print(a)

a=["geeks","for"],["geeks"]
print(a[0][1])
print(a[1][0])
print(a[0][0])

a=[1,2,3,4,5,6,7,8,9,10]
a.remove(9)
a.remove(5)
print(a)

a=[1,2,3,4,5,6,7,8,9,10]
for i in range(5,7):
    a.remove(i)
print(a)

a=[1,2,3,4,5,6,7,8,9,10]
a.pop()
print(a)
a.pop(-5)
print(a)
a.pop(5)
print(a)

a=[1,2,3,4,5,6,7,8,9,10]
print(a[::-1])#reverse list

a="geeks for geeks"
print(a[3:9])
print(a[::-1])
print(a[:5])
print(a[5:])
print(a[::])

a=['g','e','e','k','s','f','o','r','g','e','e','k','s']
print(a)
print(a[:-6])
print(a[1:9])
print(a[::-1])
print(a[-1:-6])
print(a[-6:-1])

a=("geeks","for","geeks")
print(a)
b=[1,2,3,4]
print(tuple(b))

b=tuple("geeks")
print(b)

a=(1,"geeks",2,"for",3,"geeks",4)
print(a)

a=(1,2,3)
b=("geeks","for","lavnya")
c=(a,b)
print(c)
a=("geeks")*4
print(a)

a=("geeks")
n=6
for i in range(int(n)):
     a=(a,)
print(a)

a=("lavmya","laoebbhbk","lavanya")
print(type(a))
b=[1,3.5,"love","a"]
print(type(b))
c=("hello world")
print(type(c))
d=("love",1,2.8,"a","labdvhb")
print(type(d))

a=("geeks","for","geeks")
n=4
for i in range(1,n):
    a=(a,)
print(a)

#indexing
a=("geeks",1,2,"a")
print(a[2])

#unpacking
tuple=("geeks",1,2,"a")
a,b,c,d=tuple
print(a)
print(b)
print(c)
print(d)

#concatenation
a=("geeks","for","geeks")
b=(1,23,45)
c= a + b
print(c)
#slicing
a=("geeks for geeks")
print(a[1:3])
print(a[::-1])#reverse
print(a[::-2])#reverse with gap of 1
#Print unique rows in a given boolean matrix using Set with tuples
def a(input):
    input=map(tuple,input)
result=set(input)
for row in list(result):
    print(row)
if __name__ = "__main__":
    input=[[0,1,0,0,1],[1,0,1,1,0],[0,1,0,0,1],[1,1,1,0,0]]
a(input)

shoplist=["apple","kiwi","orange","banana","mango"]
print(len(shoplist))
print(shoplist)
shoplist.append("rice")
print(shoplist)
shoplist.sort()
print(shoplist)
print(shoplist[2])
del shoplist[2]
print(shoplist)
#tuple
zoo=("dog","cat","bat","zebra")
print(len(zoo))
print(zoo)
new_zoo="elephant","tiger","lion",zoo
print(len(new_zoo))
print(new_zoo)
print(new_zoo[0])
print(new_zoo[3])
print(new_zoo[3][1])
print(len(new_zoo)-1+len(new_zoo))
#simple program
shoplist=["apple","mango","kiwi","orange"]
mylist=shoplist
print(shoplist)
print(mylist)
del shoplist[0]
print(shoplist)
print(mylist)
mylist=shoplist[:]
print(shoplist)
print(mylist)
del mylist[1]
print(shoplist)
print(mylist)
del shoplist[0]
print(shoplist)
print(mylist)
del mylist[0]
print(shoplist)
print(mylist)

a=[1,2,3,4,5]
print(sum(a))

def add(items):
    total=0
for x in items:
    total+=x
return total
print(add[1,2,3])

a=[1,2,3,4,5]
print(min(a))

a=[1221,"aba",123,"bcd","lmk"]
print(count())
a=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
a.sort()
print(a)
import datetime
now=datetime.datetime.now()
print(now.strftime("%y-%m-%d"))

r=float(input(""))
pi=3.14
area=pi*r**2
print(area)

fname=input("enter fname")
lname=input("enter lname")
print(fname + " " + lname)

a=input("enter a value")
list=a.split(",")
tuple=tuple(list)
print(list)
print(tuple)

a = ["Red","Green","White" ,"Black"]
print(a[0])
print(a[-1])
a=(11,12,2014,20)
print("%i/%i/%i/%i"%a)
exam_st_date = (11,12,2014)
print( "The examination will start from : %i / %i / %i"%exam_st_date)

n=int(input("enter a value"))
for i in range(n,n**5):
    print(i)

a=int(input("enter a value"))
n1=int("%i"%a)
n2=int("%i%i"%(a,a))
n3=int("%i%i%i"%(a,a,a))
print(n1+n2+n3)

import calendar
y=int(input("enter a year"))
m=int(input("enter a month"))
print(calendar.month(y,m))

a=('''This
is a ....... multi-line
heredoc string''')
print(a)"""

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

