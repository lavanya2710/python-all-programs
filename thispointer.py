"""str = "This is a sample String with sample message."
if "sample" not in str:
    print("yes")
else:
    print("no")


def check(list,str):
    for substr in list:
        if substr in str:
            return (substr)
    return False
str = "This is a sample String with sample message."
list=['Hello', 'here', 'with', 'here', 'who']
p=check(list,str)
print(p)
#if p[0]:
 #   print(p[1])

str = "This is a sample String with sample message."
list=['Hello', 'here', 'with', 'here', 'who']
result=any(([True if substr in str else False for substr in list]))
print(result)
#if result:
 #   print("A string from list Found in main String ")

str="hello!!"
i=len(str)-1
while i>=0:
    print(str[i])
    i-=1

str="hello!!"
i=1
while i<=len(str):
    print(str[-i])
    i+=1

str = 'This is a sample string and a sample code. It is very short.'
print(str.count("sample"))

firstStr = "SamPle is only best one"
secStr   = "sample"
if firstStr<=secStr:
    print("matching")
else:
    print("not matching")

str = "Hello, This is a sample string is is sis "
str1=str.replace("is","are",2)
print(str1)
str = "Hello, This is a sample string is is sis "
index=5
str1=str[0:index:]+str[index+1: :]
print(str1)

str = "Hello, This is a sample string is is sis"
str1=str[:-1:]
print(str1)

str = "Hello, This is a sample string is is sis"
start=5
end=10
str1=str[:start:]+str[end::]
print(str1)

str ='hello text'
if str[-1]=="t":
    print("yes")
else:
    print("no")

str ='hello text'
a=("a","q","l")
if str.endswith(a):
    print("yes")
else:
    print("no")

from collections import Counter
str = 'This is a sample string and a sample code. It is a very short string. 001122'
frequency=Counter(str)
for (key,values) in frequency.items():
    print(key,values)

from collections import Counter
str = 'This is a sample string and a sample code. It is a very short string. 001122'
frequency=Counter(str)["s"]
print(frequency)

list=["hi"]*20
print(list)
list=["hi" for i in range(20)]
print(list)

list=[1,2,3,4,5]
list.append(6)
list.append([7,8,9,10])
print(list)
list.extend([1,2,3,4,5])
print(list)
list.insert(0,7)
print(list)

list1 = ['city', 'Hi', 'hello', 'at', 'why', 'this', 'there', 'from']
list2 = [3,5,7,1]
list=list1[:3]+list2[:]+list1[4:]
print(list)

list=[1,2,3,4,5]
for i in list:
    print(i)

list=["hi","hello","how","are","you"]
i=0
while i<len(list):
    print(list[i])
    i=i+1

list=["hi","hello","how","are"]
for i in range(len(list)):
    print(list[i])

list=[1,2,3,4,5,"hi","hello","how","are","you"]
list.remove("hi")
print(list)

list=[1,2,3,4,5,"hi","hello","how","are","you"]
list.pop()
print(list)

list=[1,2,3,4,5,"hi","hello","how","are","you"]
del list[1]
print(list)
list=[10, 2, 45, 3, 5, 7, 2 , 10, 45,  8, 10]
list1=set(list)
print(list1)

list=[12, 44, 56, 45, 34, 3, 4, 33, 44]
for i in list:
    if i%3==0:
        list.remove(i)
print(list)

list=[12, 44, 56, 45, 34, 3, 4, 33, 44]
del list[1:4]
print(list)

list= ['Hello', 'Ok', 'is', 'Ok', 'test', 'this', 'is', 'a', 'test', 'Ok']
ele="Ok"
p=list.index(ele)
print(p)
list= ['Hello', 'Ok', 'is', 'Ok', 'test', 'this', 'is', 'a', 'test', 'Ok']
index=[i for i in range(len(list))if list[i]=="Hello"]
print(index)
list=[1,2,3,4,5,6,7,8,9]
ele=5
pos=-1
for i in range(len(list)):
    if list[i]==ele:
        pos=i
        break
if pos>-1:
    print(pos)
else:
    print(pos)

list=[1,2,3,4,5,6,7,8,9]
ele=9
pos=len(list)-list[::-1].index(ele)-1
print(pos)
list=['Hi' , 'hello', 'at', 'this', 'there', 'from']
if "hi" not in list:
    print("yes")
else:
    print("no")
list=['hi' , 'hello', 'at', 'this', 'there', 'from']
list.sort()
print(list)
list=['hi' , 'hello', 'at', 'this', 'there', 'from']
list.sort(reverse=True)
print(list)
list=['hi' , 'hello', 'at', 'this', 'there', 'from']
list.sort(key=len)
print(list)
list= [ ('the' , 34) , ('at' , 23), ('should' , 1) , ('from' , 3) ]
list.sort(key =lambda ele: ele[1])
print(list)
list1 = ["This" , "is", "a", "sample", "program"]
list2 = [10, 2, 45, 3, 5, 7, 8, 10]
#list3=list1+list2
#print(list3)
list1.extend(list2)
print(list1)

list= [ [1,2,3,45,6,7],[22,33,44,55],[11,13,14,15]]
count=0
for i in list:
    count=count+len(i)
print(count)

tup=('a',1,"b","c","d")
tup=tup+(5,)
print(tup)

#global variable
a=5
def b():
    global a
    a=15
    print(a)

    a=10
    print(a)
b()
print(a)

def func(a,*b):
    c=a
    for i in b:
        c=c+i
    print(c)
func(5,6,11,7)

def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)
person(name="love",age=23,city="bang",pin=95)
dict={'Jack': 32, 'Ritika': 31, 'Mark' : 22, 'Mathew' : 27}
age=dict["Jack"]
print(age)

list=["Hello", "hi", "there", "at", "this"]
dict1=dict.fromkeys(list,0)
print(dict1)

dict={'Jack': 32, 'Ritika': 31, 'Mark' : 22, 'Mathew' : 27}
for i in dict:
    j=dict[i]
    print(i,"::",j)


def sort1(a):
    if len(a)>1:
        mid=(len(a))//2
        l=a[:mid]
        r=a[mid:]
        sort1(l)
        sort1(r)
        i=j=k=0
        while i<len(l) and j<len(r):
            if l[i]<r[j]:
                a[k]=l[i]
                i=i+1
            else:
                a[k]=r[j]
                j=j+1
            k=k+1
        while i<len(l):
            a[k]=l[i]
            i=i+1
            k=k+1
        while j<len(r):
            a[k]=r[j]
            j=j+1
            k=k+1
#main
a=[1,0,0,1,0,1,1,0,1]
sort1(a)
print(a)

n=54321
rev=0
while n>0:
    a=n%10
    rev=rev*10+a
    n=n//10
print(rev)"""

a=[1,2,7,3,4,5]
a.sort()
print(a)




