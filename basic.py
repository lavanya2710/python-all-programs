"""name=(input("enter something"))
print("hello",name)


def getstring():
    result=int(input("enter a value"))
    return result
def b():
    print("vhsndb")
output=getstring()
print(output)

if __name__=="__main__":
    b()

for i in range(5):
    print(i)

for i in range(1,5):
    print(i)

#module
import math
def a():
    num=float(input("enter a value"))
    num=math.fabs(num)
    print(num)
if __name__=="__main__":
    a()

a=[1,2,3]
print(a)
del a[1]
print(a)
assert 5>3

#global

count=6
def fun():
    global count
count=count+1
print(count)
fun()

x=7
def fun():
    global x
x=2
print(x)
fun()
#local
x=2
def fun():
    print(x)
x=7
print(x)
fun()

#scope of an object
def some_func():
    print("inside a")
def some_inner_func():
    a=10
    print(a)
some_inner_func()
print(a)
some_func()

#whitespace
x=[1,2,3]
y=4
a= y in x
print(a)

#list of keywords
import keyword
print("a")
print(keyword.kwlist)

#direct initialising
a=7
print("the value of a is:",a)

#conditional initialising
a=10 if 20>10 else 0
print("the value of a is:",a)

#next line
print("hello")
print("bangalore")

print("hello"); print("world")

print("hello",end=" "),
print("world")

a=[1,2,3,4]
for i in range(4):
    print(a[i],end=" ")

a=int(input("enter a num"))
print(a)
print(type(a))

x,y= input("enter a value:").spilt()
print("print a value:",x)
print("print a value:",y)
print()

x,y=[int(x) for x in input("enter a  value").split()]
print(x)
print(y)
print()

x=[int(x) for x in input("enter a value").split(",")]
print(x)

#output
print("welcome",end=" ")
print("world",end=" ")

print("hello",end="@")
print("world",end=" ")

print('G','F','G', sep='') 
print("hello","world",sep="@")
print("hello","world",sep="@",end=" ")

print( "i love {1} for {0}".format("geeks","geeks"))

#strings
a=("lavanya is working on python")
print(a)
#list
list=[1,1+2,"a",0.5,"lavanya"]
print(list)
list.append(3)
print(list)
list.pop()
print(list)
print(list[0])
#tuple
a=[1,"a",0.2,"love"]
print(a[2])
#while
i=1
while (i<10):
    i=i+1
    print (i)

i=10
while (i<20):
    i=i-1
print(i)

s=("hello world")
for i in s:
    print(i)

def a():
    result=(input("enter a value"))
    return result
def b():
    print("lavanya")
output= a()
print(output)

if __name__ == "__main__":
    b()

i=6
while i<6:
    print(i)
    i +=1

a=("lavanya")[::-1]
print(a)

a="lavanya"
print(a[::-1])

a="  lavanya   "
print(len(a))

a="   lavanya  "
print(a.strip())

a="   lavanya  "
print(a.lstrip())

a="     lavanya      "
print(a.rstrip())

a="lavaNYA"
print(a.lower())

a="lavanya"
print(a.upper())

a="laVANya"
print(a.swapcase())

a="lavanya sbvhsnkc bvsmhshb"
print(a.replace("a","l"))

a="lavanya fnskfkls fishfkjjakl"
print(a.split(","))

n=int(input(""))
if 1<=n<=20:
    print ("yahoo")


n=int(input(""))
if (n%2!=0):
    print("Weird")
elif (n%2==0 and 2<=n<=5):
    print("Not Weird")
elif (n%2==0 and 6<=n<=20):
    print("Weird")
elif (n%2==0 and n>20):
    print("Not Weird")
else:
    print("invalid input")

a=int(input("enter a value"))
b=int(input("enter b value"))
print(a+b)
print(a-b)6564424525
print(a*b)

a=int(input(""))
b=int(input(""))
print(a//b)
print(a/b)

for i in range(0,3):
    print(i**2)


print("hello",end='')
print("hello")

n=int(input())
for i in range(1,n+1):
    print(i,end="")

a=str(input())
print(str.swapcase(a))

a=str(input())
print(str.istitle(a)!=0)


print("helo" in "car is going on the road")

print("hello guys how are you".find("you"))
print("hello guys how are you".find("world"))
print("hello guys how are you".index("you"))
print("hello guys how are you".index("world"))

a=str(input())
print(a.count("y"))

a=str(input())
print(a.capitalize())

a="lavaNYA"
b=52
print("{} age is {}".format(a,b))

a=2
print("a".isnumeric())

print("lavya is great".split(" "))

print("lavya is great".islower())
print("lavya is great".isupper())

print("lavya is great"[4].islower())

a="hello world"
print(a[::-1])

a="AA129"
print(a.isascii())

a="fish"
print("a"[0].upper+"a"[1:-1].upper+"a"[-1].upper)

print(str(5))

a="hello world i am very happy for learning python"
print(a.replace("i","we", "learning","we"))

a="lavaNYA"
print(max(a))

a="lavnya is best "
print(a.startswith("lav"))
print(a.endswith("kal"))

a=" hello "
print(a.isspace())

a=" hello "
print(a*3)

a=" hello "
b="world"
print(a + b)

a= 'Hello 1 World 2'
vowels = ('a','e','i','o','u')
print(''.join([ d for d in a if d in vowels]))

a="how are you i am you and you you are you you"
print(a.rfind("you")) 
a="how are you i am you and you you are you you"
print(a.find("you")) 

import operator
a=3
b=4
if (operator.le(a,b)):
    print("a is less than b")
elif (operator.le(a,b)):
    print("a is less than or equal to b")
elif(operator.eq(a,b)):
    print("a is equal to b")
    
a=[1,2,3,4,5]
print(max(a))

def arrayManipulation(n, queries):
    array = [0] * (n + 1)
    
    for query in queries: 
        a = query[0] - 1
        b = query[1]
        k = query[2]
        array[a] += k
        array[b] -= k
        
    max_value = 0
    running_count = 0
    for i in array:
        running_count += i
        if running_count > max_value:
            max_value = running_count
            
    return max_value"""

a=[1,2,3,4,5]
print(a[0:3])