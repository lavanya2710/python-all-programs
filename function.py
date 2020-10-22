"""def say_hello():
    print("hello world")
    say_hello()
    say_hello()

def f():
    print(s)
s="lavanya"
print(s)

def f():
    s="mee too"
    print(s)
s="lavanya"
f()
print(s)

def f():
    print(s)
   
    print(s)
s="lavanya"
print(s)
f()
print(s)

def f():
    global s
    print(s)
    s="lavanya"
    print(s)
s="python"
f()
print(s)

a=1
def f():
    print(a)
def g():
    a=2
    print(a)
def h():
    a=3
    print(a)
print(a)
f()
print(a)
g()
print(a)
h()

def fun(a):
    print(a)
mylist=[1,2,3,4]
fun(mylist)

def fun(a,b,c,d):
    print(a,b,c,d)
mylist=[1,2,3,4]
fun(*mylist)

def mySum(*args):
    Sum=0
    for i in range(0, len(args)):
        Sum =Sum + args[i]
        return Sum
print(mySum(1, 2, 3, 4, 5)) 
print(mySum(10, 20)) 

def fun(a,b,c):
    print(a,b,c)
d={"a":2,"b":3,"c":4}
fun(1,**d)

s="10010"
c=int(s,2)
print(c)
e=float(s)
print(e)

s="4"
c=ord(s)
print(c)
c=hex(56)
print(c)
c=oct(56)
print(c)

s="geeks"
c=tuple(s)
print(c)
c=set(s)
print(c)
c=list(s)
print(c)

a=1
b=2
tup=(("a",1),("b",2),("c",3))
c=complex(a,b)
print(c)
c=str(a)
print(c)
c=dict(tup)
print(c)

a=chr(75)
b=chr(76)
print(a)
print(b)

x = int(input())
y = int(input())
z = int(input())
n = int(input())
print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if sum([i,j,k]) != n])

if __name__ == '__main__':
    n =[2,3,6,6,5]
    print(n.max)
    print(n.min)

year=int(input(""))
if year%4==0:
    return True
elif year%100==0:
    return False
elif year%4==0:
    return True    
else:
    return False

a=[2,3,6,6,5]
print(max(a))
print(max(a)-1)
#encode str to byte obect
a="geeks for geeks"
c=b"geeks for geeks"
d=a.encode("ASCII")
if(d==c):
    print("encoding sucessfully")
else:
    print("encoding unsuccesfully")
#decode byte object to string
a="geeks for geeks"
c=b"geeks for geeks"
d=c.decode("ASCII")
if (d==a):
    print("decode successfully")
else:
    print("decode failed")
#single variable multi variable
print(1)
print((1))
print(1,2)
print((1,2))
#swap two variables
x=5
y=10
x,y=y,x
print(x,y)
#private variable
class map:
    def _init_(self,iterate):
        self.list=[]
        self._geek(iterate)
def geek(self,iterate):
    for item in iterate:
        self.list.append(item)
        _geek=geek
class mapsubclass:
    def geek(self,key,values):
        for i in zip(key,values):
            self.list.append(i)
#single leading underscore
def _geterrors(self):
    if self.errors is none:
        self.full_clean()
        return self._errors
        errors=property(_get_errors)

#double leading underscore
class geek:
    def _single_method(self):
        pass
    def __double_method(self):
        pass
class pyth(geek):
    def __double_method(self):
        pass
class geek:
    def__init__(self,ab):
    self.ab=ab
    def__custom__(self):
    pass

if __name__=="__main__":
    print("yes")
else:
    print("no")

a,b=10,20
min= a if a<b else b
print(min)

a,b=10,20
#tuple
print((b,a)[a<b])
#dictionary
print({True:a,False:b}[a<b])
#lambda
print((lambda:b,lambda:a)[a<b]())

a,b=10,20
min=a<b and a or b
print(min)

class complex:
    def _init_(self,a,b):
        self.a=a
        self.b=b
    def _add_(self,other):
        return self.a+other.a,self.b+other.b
    def _str_(self):
        return self.a,self.b
    ob1=complex(1,3)
    ob2=complex(2,4)
    ob3=ob1+ob2
    print(ob3)

class A:
    def __init__(self,a):
        self.a=a
    def __gt__(self,other):
        if(self.a>other.a):
            return True
        else:
            return False
ob1= A(2)
ob2= A(3)
if(ob1>ob2):
    print("ob1 is greater than ob2")
else:
    print("ob1 is lesser than ob2")

n=int(input(" "))
for i in range(1,n):
    print(i)

list1=[]
list2=[]
for i in range(1,11):
    list1.append(4*i)
for i in range(0,9):
    list2.append(list1[i]%5==0)
print(all(list2))
list1=[]
list2=[]
for i in range(1,21):
    list1.append(4*i-3)
for i in range(0,20):
    list2.append(list1[i]%2==1)
print(all(list1))

n=[2,3,6,6,5]
a= map(int, input().split())
print (sorted(set(a))[-3])

n=[2,3,6,6,5]
s=set(n)
s.remove(max(s))
print(max(s))


list=[]
list.insert(0,5)
list.insert(1,10)
list.insert(0,6)
print(list)
list.remove(6)
list.append(9)
list.append(1)
list.sort()
print(list)
list.pop(-1)
print(list[::-1])

n= int(input())
L=[]
for i in range(n):
    args = input().strip().split(" ")
    if args[0] == "append":
        L.append(int(args[1]))
    elif args[0] == "insert":
        L.insert(int(args[1]), int(args[2]))
    elif args[0] == "remove":
        L.remove(int(args[1]))
    elif args[0] == "pop":
        L.pop()
    elif args[0] == "sort":
        L.sort()
    elif args[0] == "reverse":
        L.reverse()
    elif args[0] == "print":
        print (L)"""
tup=(1,2,3,4)
a,b,c,d=tup
print(tup)



