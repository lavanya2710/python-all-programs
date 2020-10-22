"""for i in range(0,5):
    for j in range(0,i):
        print("*",end=" ")
        print("\n")
        i=i+1
rows = 6
for num in range(rows):
    for i in range(num):
        print(num, end=" ")   


class a:
    def __init__(self):
        print("hello")
    def b(self):
        print("world")

obj=a()
obj.b()

class a:
    def __init__(self,ai,b):
        self.ai=ai
        self.b=b
    def bi(self):
        print("hello",self.ai,self.b)
obj=a(5,6)
obj.bi()

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
obj.age=30
obj1=a()
if obj.compare(obj1):
    print("same")
else:
    print("different")
obj.name="love"
print(obj.name)
print(obj.age)
print(obj1.name)
print(obj1.age)

class student:
    school="lpu"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def average(self):
        return(self.m1+self.m2+self.m3)/3
    @classmethod
    def info(cls):#class method
        return cls.school
    @staticmethod
    def inf():#static method
        print("hello")
    def get_m1(self):
        return self.m1
    def set_m1(self,values):
        self.m1=values
s1=student(1,2,3)
s2=student(10,15,19)
print(s1.average())
print(s1.get_m1())#accessor
print(s2.set_m1(5))#mutator
print(s2.m1,s2.m2,s2.m3)
print(student.info())
student.inf()
#inheritance
class a:
    def feature1(self):
        print("feature1 is working")
    def feature2(self):
        print("feature1 is working")
class b():
    def feature3(self):
        print("feature1 is working")
    def feature4(self):
        print("feature1 is working")
class c(a,b):
    def feature4(self):
        print("feature1 is working")
    def feature5(self):
        print("feature1 is working")
obj=a()
obj1=b()
obj2=c()
obj2.feature1()
obj.feature1()

class a:
    def __init__(self):
        print("hello")
    def feature1(self):
        print("feature1 is working")
    def feature2(self):
        print("feature1 is working")
class b(a):
    def __init__(self):
        super().__init__()
        print("world")
    def feature3(self):
        print("feature1 is working")
    def feature4(self):
        print("feature1 is working")

a1=b()


class a:
    def __init__(self):
        print("hello")
    def feature1(self):
        print("feature1 is working")
    def feature2(self):
        print("feature1 is working")
class b():
    def __init__(self):
        print("world")
    def feature3(self):
        print("feature1 is working")
    def feature4(self):
        print("feature1 is working")
class c(a,b):
    def __init__(self):
        print("hi")
    def feature4(self):
        print("feature1 is working")
    def feature5(self):
        print("feature1 is working")

a1=c()


a="this is where you are using everything for evryone but you are choosing this"
print(a.index("this",5,100))

a="lavanya"
b=23
print("my name is {} age is {}".format(a,b))

a="this is lavanya how can i asset uh".split(" ")
print(a)
a="hello world"
print(a[::-1])
a="fish"
print(a[0].upper()+a[1:-1]+a[-1].upper())
a="this is where you are using everything for evryone but you are choosing this"
print(a[0:5])
a="5"
print(type(a))
a="this is where you are using"
print(a.replace("this","you"))
print(min("abcd"))
a="lavanya"
print(a*3)
a="lava"
b="nya"
print(a+""+b)
a="this is you you is this that is this ok byeee world"
b=(a.maketrans("this","THI$"))
print(a.translate(b))
a="hello world"
vowels="a","i","e","o","u"
print("".join([b for b in a if b not in vowels]))
a=[1,2,3,4,5,7]
b="".join(a)
print(b)
a=[1,2,3,4,5,6,7,5,9,8]
a.sort()
print(a)
a=[1,2,3,4]
b=a[:]
print(b)

set1=set((1,2,3.5,4,56,5,5,5,5,5,6))
set1.add(99)
print(set1)
i=0
while i<10:
    i=i+1
    print(i)

for i in range(0,11):
    print(i)

n=5
for i in range(0,5):
    for j in range(1,i+1):
        print(j,end=" ")
        i=i+1
    print(" ")
sum=0
n=int(input("enter a value"))
for i in range(1,n):
    sum+=i
print(sum)

n=2
for i in range(1,11):
     mul=i*n
     print(mul)

list = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
for i in list:
    if i>150:
        break
    if i%5==0: 
        print(i)
num = 72555
count = 0
while num != 0:
    num //= 10
    count+= 1
print(count)
list=[1,2,3,5,6,7]
for i in reversed(list):
    print(i)
for i in range(-10,0):
    print(i)

for i in range(5):
    print(i)
print("done!")
start=25
end=50
for num in range(start,end+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
                print(num)
a=0
b=1
print(a)
print(b)
for i in range(2,10):
    c=a+b
    a=b
    b=c
    print(c)
f=1
n=5
for i in range(1,n+1):
    f=f*i
print(f)
s="847983"
print(s[::-1])

list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in list[1::3]:
    print(i)

def fac(x):
    f=1
    for i in range(1,x+1):
        f=f*i
    return f
n=6
result=fac(n)
print(result)

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

n=7
for i in range(2,n):
    if n%i==0:
        print("not prime")
        break
    else:
        print("prime")
        break"""

