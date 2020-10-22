"""def pypat(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end=" ")
        print("\r")
n=5
pypat(n)

def pypat(n):
    mylist=[]
    for i in range(1,n+1):
        mylist.append("*"*i)
        print("\n".join(mylist))
n=5
pypat(n)

def pypart(n):
    k=2*n-2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k=k-2
        for j in range(0,i+1):
            print("*",end=" ")
        print("\r")
n=5
pypart(n)

def pypart(n):
    k=2*n-2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k=k-1
        for j in range(1,i+1):
            print("*",end=" ")
        print("\r")
n=5
pypart(n)

def numpat(n):
    num=1
    for i in range(0,n):
        num=1
    for j in range(0,i+1):
        print(num,end=" ")
        num=num+1
    print("\r")
n=5
numpat(n)

def countnum(n):
    num=1
    for i in range(0,n):
        for j in range(0,i+1):
            print(num,end="")
        num=num+1
    print("\r")
n=5
countnum(n)

def alpha(n):
    num=65
    for i in range(0,n):
        for j in range(0,i+1):
            ch=chr(num)
            print(ch,end="")
            num=num+1
            print("\r")
n=5
alpha(n)

def evennum(l):
    for ele in l:
        if ele%2==0:
            print("list contains even numbers")
            break
        else:
            print("not contains even numbers")
evennum([1,2,3,8,10])
evennum([4,6,8,5,9])

count=0
while(count<1):
    count=count+1
    print(count)
    break
else:
    print("no else")

def numbers_to_strings(argument): 
    switcher = { 
        0: "zero", 
        1: "one", 
        2: "two", 
    } 
    return switcher.get(argument,"nothing")
if __name__=="__main__":
    argument=0
    print numbers_to_strings(argument)"""
























































