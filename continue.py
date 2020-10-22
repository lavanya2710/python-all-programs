"""for i in range(1,10):
    if i<=5:
        print("correct")
        continue
    print("try again")


def say_hello():
    print("hello world")
say_hello()
say_hello()
say_hello()

def say_hello():
    print("hello world")
def b():
    print("main main")
if __name__=="__main__":
    say_hello()
    b()

#function parameter
def calc(a,b):
    if a<b:
        print("a is minimum")
    elif a>b:
        print("a is maximum")
    else:
        print("a is equal to b")
    
calc(3,3)

#function argument
x=4
y=6
calc(x,y)

#local variable
x=10
def fun(x):
    print(x)
x=20
print(x)
fun(x)
print(x)

#global variable
c=5
def fun():
    global c
print(c)
c=2
print(c)
fun()
print(c)

#default argument
def fun(msg,time=5):
    print(msg*time)
fun("hello")
fun("world",7)

#keyword argument
def func(a,b=45,c=100):
    print("a is",a,"b is",b,"c is",c)
func(23,26)
func(a=65,c=8)
func(c=28,a=95)

#return statements
def maximum(x,y):
    if x>y:
        return x
    elif x==y:
        return"equal"
    else:
        return y
print maximum(9,7)"""


#docstring

def print_max(x,y):
    
    x=int(x)
    y=int(y)
if x>y:
    print(x,"is maximum")
else:
    print(y,"is maximum")
print(3,4)
print(print_max.__doc__)








    









