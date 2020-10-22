"""#add two nums
a=5
b=10
c=a+b
print(c)

def add(a,b):
    a=5
    b=10
    c=a+b
    return c
result=add(a,b)
print(result)

#maximum of two nums
a=2
b=4
if a>b:
    print(a)
else:
    print(b)

a=2
b=4
maximum=max(a,b)
print(maximum)

def fac(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
x=5
result=fac(x)
print(result)

def fac(n):
    if n==0:
        return 1
    return n * fac(n-1)
result=fac(5)
print(result)

P = 10000
R = 5
T = 5
si=P*R*T/100
print(si)

for i in range(0,10):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)

num=10
if num>1:
    for i in range(2,num):
        if num%i==0:
            print("not prime")
            break
        else:
            print("prime")
            break
    else:
        print("prime")

def fib(n):
    a=0
    b=1
    if n<0:
        print("invalid")
    elif n==0:
        return a
    else:
        for i in range(2,n):
            c=a+b
            a=b
            b=c
        return b
print(fib(9))

def sum1(arr,n):
    return sum(arr)
arr=[]
arr=[1,2,3,4]
n=len(arr)
ans=sum1(arr,n)
print(ans)

def maximum(arr,n):
    max=arr[0]
    for i in range(1,n):
        if arr[i]>max:
            max=arr[i]
    return max
arr=[1,2,3,4,5]
n=len(arr)
ans=maximum(arr,n)
print(ans)

list=[5,3,2,1,4]
for i in range(len(list)):
    min_val=min(list[i:])
    min_index=list.index(min_val)
    list[i],list[min_index]=list[min_index],list[i]
print(list)

arr=[6,4,32,4,2,33]
for j in range(len(arr)-1):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
print(arr)

def merge(arr):
    if len(arr)>1:
        mid=len(arr)//2
        l=arr[:mid]
        r=arr[mid:]
        merge(l)
        merge(r)
        i=j=k=0
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
arr=[50,30,20,10,40]
merge(arr)        
print(arr)

#linear search
def linear(arr,key):
    arr1=[]
    flag=False
    for i in range(len(arr)):
        if key==arr[i]:
            flag=True
            arr1.append(i)
    if flag==True:
        print("found",i)
    else:
        print("not found")

list=[50,30,20,10,40]
key=50
linear(arr,key)

#binar search
mid=low+high//2
if key==mid:
return mid
else key>mid
return low=mid+1
elif 
return high=mid-1

def leftrot(arr,d,n):
    for i in range(d):
        leftrotbyone(arr,n)
def leftrotbyone(arr,n):
    temp=arr[i]
    arr[i]=arr[i+1]

arr=[1,2,3,4,5]
leftrot(arr,2,5)
printarray(arr,5)




def insertion(list):
    for i in range(1,len(list)):
        cur=list[i]
        pos=i
        
        while cur<list[pos-1] and pos>0:*
            list[pos]=list[pos-1]
            pos=pos-1
            list[pos]=cur
        print(i, ':', list)
list=[5,3,4,1,2]
print('----',list)
insertion(list)
print(list)

def mergesort(list1):
    if len(list1)==1:
        return list1
    if len(list1)>1:
        mid=len(list1)//2
        left_list=list1[:mid]
        right_list=list1[mid:]
        mergesort(left_list)
        mergesort(right_list)
        i=j=k=0
        while i<len(left_list) and j<len(right_list):
            if left_list[i]<right_list[j]:
                list1[k]=left_list[i]
                i=i+1
                k=k+1
            else:
                list1[k]=right_list[j]
                j=j+1
                k=k+1
        while i<len(left_list):
            list1[k]=left_list[i]
            i=i+1
            k=k+1
        while j<len(right_list):
            list1[k]=right_list[j]
            j=j+1
            k=k+1
list1=[5]
#list1=[5,4,6,3,1,2,7,9,8]
mergesort(list1)
print(list1)

def insertion(my_list):
    for i in range(1,len(my_list)):
        cur_ele=my_list[i]
        pos=i
        while cur_ele<my_list[pos-1] and pos>0:
            my_list[pos]=my_list[pos-1]
            pos=pos-1
        else:
            my_list[pos]=cur_ele
list1=[5,4,6,3,1,2,7,9,8]
insertion(list1)
print(list1)

def maximum(arr,n):
    max=arr[0]
    for i in range(1,n):
        if arr[i]>max:
            max=arr[i]
    return max

arr=[43,24,52,566,19987]
n=len(arr)
ans=maximum(arr,n)
print(ans)

def leftrotation(arr,d,n):
    for i in range(0,d):
        leftrotationbyone(arr,n)
def leftrotationbyone(arr,n):
    temp=arr[0]
    for i in range(0,n-1):
        arr[i]=arr[i+1]
    arr[n-1]=temp

arr=[1,2,3,4,5]
leftrotation(arr,2,5)
print(arr)

def leftrot(arr,d,n):
    for i in range(d):
        leftrotbyone(arr,n)
def leftrotbyone(arr,n):
    temp=arr[0]
    for i in range(0,n-1):
        arr[i]=arr[i+1]
    arr[n-1]=temp
arr=[12, 10, 5, 6, 52, 36]
leftrot(arr,2,6)
print(arr)

def findremainder(arr,lens,n):
    mul=1
    for i in range(0,lens):
        mul=(mul*(arr[i]%n)%n)
    return mul%n

arr=[100, 10, 5, 25, 35, 14]
lens=len(arr)
n=11
result=findremainder(arr,lens,n)
print(result)

def monotic(a):
    return (all(a[i]<=a[i+1] for i in range(len(a)-1) or
           all(a[i]>=a[i+1] for i in range(len(a)-1))))
a=[5,4,3,3]
print(monotic(a))

def swaplist(newList):
    size=len(newList)
    temp=newList[0]
    newList[0]=newList[size-1]
    newList[size-1]=temp
    return newList
newList = [12, 35, 9, 56, 24] 
op=swaplist(newList)
print(op)

def swap(newlist):
    newlist[0],newlist[-1]=newlist[-1],newlist[0]
    return newlist
newlist= [12, 35, 9, 56, 24] 
op=swap(newlist)
print(op)

def swap(arr,pos1,pos2):
    arr[pos1],arr[pos2]=arr[pos2],arr[pos1]
    return arr
arr=[23, 65, 19, 90] 
pos1,pos2=1,3
res=swap(arr,pos1,pos2)
print(res)
def length(list):
    count=0
    for i in list:
        count=count+1
    return count
list=[1,2,3,4,5]
res=length(list)
print(res)

test_list = [ 1, 6, 3, 5, 3, 4 ]
for i in test_list:
    if i==4:
        print("found",i)
    else:
        print("not found")

list1=[1,2,3,4,5]
list1.clear()
print(list1)
    
list = [10, 11, 12, 13, 14, 15]
for i in reversed(list):
    print(i),
print(list[::-1])

list = [10, 11, 12, 13, 14, 15]
for i in range(len(list)-1,-1,-1):
    print(list[i]),

list=[12, 15, 3, 10]
total=0
for i in range(len(list)):
    total=total+list[i]
print(total)
list=[12, 15, 3, 10]
total=sum(list)
print(total)
i=0
total=0
list=[12, 15, 3, 10]
while(i<len(list)):
    total=total+list[i]
    i=i+1
print(total)
list=[1,2,3]
total=1
for i in range(len(list)):
    total=total*list[i]
print(total)

list1 = [10, 20, 4]
list1.sort()
print(list1[0])
print(min(list1))

list1 = [10, 20, 4,13,29,74,809,456]
list1.sort()
print(list1[-1])
print(max(list1))
print(list1[-2])
#n largest
list1=[4, 5, 1, 2, 9]
n=2
list1.sort()
print(list1[-n:])

def largest(list,n):
    finallist=[]
    for i in range(0,n):
        max=0
        for j in range(len(list)):
            if list[j]>max:
                max=list[j]
        list.remove(max)
        finallist.append(max)
    return finallist
list=[4, 5, 1, 2, 9]
n=2
res=largest(list,n)
print(res)

list1 = [2, 7, 5, 64, 14]
for i in list1:
    if i%2==0:
        print(i),

list1 = [2, 7, 5, 64, 14]
for i in list1:
    if i%2==1:
        print(i),

for i in range(10):
    if i%2==0:
        print("even",i),
for i in range(10):
    if i%2==1:
        print("odd",i),

list1 = [12, -7, 5, 64, -14]
for i in list1:
    if i>=0:
        print(i)

for i in range(-4,5):
    if i>=0:
        print(i),

for i in range(-4,5):
    if i<=0:
        print(i),

list=[12, 15, 3, 10]
list.remove(12)
list.remove(3)
print(list)

list=[5, 6, [], 3, [], [], 9]
list.remove([])
print(list)

list=[5, 6,4,5,6,9]
list1=list
print(list1)

list=[5, 6,4,5,6,9]
list1=list[:]
print(list1)

lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
print(lst.count(10))

lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
x=10
count=0
for i in lst:
    if i==x:
        count=count+1
print(count)

a="and"
list1=list(a)
print("".join(list1))

list=[10,20,30,40,50]
newlist=[]
j=0
for i in range(len(list)):
    j=j+list[i]
    newlist.append(j)
print(newlist)

x= [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
 
y= [[9,8,7],
    [6,5,4],
    [3,2,1]]

result=[[0,0,0],
        [0,0,0],
        [0,0,0]]
for i in range(len(x)):
    for j in range(len(y[0])):
        result[i][j]=x[i][j]+y[i][j]
for r in result:
    print(r)

x= [[1,2],[3,4]]
 
y= [[4,5],[6,7]]

result=[[0,0],
        [0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j]=x[i][j]-y[i][j]
for r in result:
    print(r)

n=10
queries=[[1,5,3],[4,8,7],[6,9,1]]
a=[0]*n
for i in queries:
    print(queries[0:1]+queries[2])

dict1={1:"lava",2:"love",3:"lav"}
print(dict1.keys())
print(dict1.values())

dict1={1:"lava",2:"love",3:"lav"}
for x in dict1:
    print(x)
for x in dict1.values():
    print(x)
for x,y in dict1.items():
    print(x,":",y)

def fizzBuzz(n):
    for i in range(1,n):
        if i%3==0 and i%5==0:
            print("FizzBuzz")
        elif i%3==0 and i%5!=0:
            print("Fizz")
        elif i%5==0 and i%3!=0:
            print("Buzz")
        else:
            print(i)
if __name__ == '__main__':
    n = 15
    fizzBuzz(n)

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the countTriplets function below.
def countTriplets(arr, r):
    r2 = Counter()
    r3 = Counter()
    r4=Counter()
    count = 0
    
    for v in arr:
        if v in r4:
            count += r4[v]
        
        if v in r3:
            r4[v*r] += r3[v]
        
        if v in r2:
            r3[v*r]+=r2[v]
        else:
            r2[v*r] += 1

    return count

if __name__ == '__main__':

    n = int(input("hsjh"))

    r = int(input("hsjh"))

    arr = [1,3,9,9,27,81]

    ans = countTriplets(arr, r)
    print(ans)

from collections import Counter
# Complete the freqQuery function below.
def freqQuery(queries):
    freq = Counter()
    cnt = Counter()
    arr = []

    for q in queries:
        if q[0]==1:
            cnt[freq[q[1]]]-=1
            freq[q[1]]+=1
            cnt[freq[q[1]]]+=1

        elif q[0]==2:
            if freq[q[1]]>0:
                cnt[freq[q[1]]]-=1
                freq[q[1]]-=1
                cnt[freq[q[1]]]+=1

        else:
            if cnt[q[1]]>0:
                arr.append(1)
            else:
                arr.append(0)

    return arr

def freqQuery(queries):
    d1 = Counter()#freq
    d2 = Counter()#cnt
    result = []#arr

    for op,val in queries:
        if op==1:
            d2[d1[val]-=1
            d1[val]+=1
            d2[d1[val]]+=1

        elif op==2:
            if d1[val]>0:
                d2[d1[val]]-=1
                d1[val]-=1
                d2[d1[val]]+=1

        else:
            if d2[val]>0:
                result.append(1)
            else:
                result.append(0)

    return result

def superDigit(n, k):
    def sum_digit(v):
        if v<10:
            return v
        s=sum(int(i) for i in str(v))
        return sum_digit(s)
    x=sum_digit(int(n))
    return superDigit(x*k)


class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def push(self,new_data):
        new_node=node(new_data)
        new_node.next=self.head
        self.head=new_node
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
#main
llist=linkedlist()
llist.head=node(1)
second=node(2)
third=node(3)
llist.push(4)
llist.head.next=second
second.next=third
llist.printlist()

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def push(self,new_data):
        new_node=node(new_data)
        new_node.next=self.head
        self.head=new_node
    def insertafter(self,prev_node,new_data):
        if prev_node is None:
            return
        new_node=node(new_data)
        new_node.next=prev_node.next
        prev_node.next=new_node
    def append(self,new_data):
        new_node=node(new_data)
        if self.head is None:
            self.head=new_node
            return 
        else:
            last=self.head
            while(last.next):
                last=last.next
            last.next=new_node

    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data),
            temp=temp.next
#main

llist=linkedlist()
llist.append(5)
llist.append(4)
llist.push(1)
llist.push(2)
llist.insertafter(llist.head.next,3)
llist.printlist()

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def push(self,new_data):
        new_node=node(new_data)
        new_node.next=self.head
        self.head=new_node
    def delete(self,key):
        temp=self.head
        if (temp is not None):
            if (temp.data==key):
                self.head=temp.next
                temp=None
                return
        while(temp is not None):
            if (temp.data==key):
                break
            prev=temp
            temp=temp.next
        if temp==None:
            return 
        prev.next=temp.next
        temp=None
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data),
            temp=temp.next
#main
llist=linkedlist()
llist.push(3)
llist.push(4)
llist.push(5)
llist.push(6)
llist.delete(5)
llist.printlist()

def delete(self,position):
    temp=self.head
    if temp is None:
        return
    if position==0:
        temp=temp.next
        temp=None
        return
    for i in range(position-1):
        temp=temp.next
        if temp is None:
            break
    if temp is None:
        return
    if temp.next is None:
        next=temp.next.next
        temp.next=None
        temp.next=next
def delete(self):
    cur=self.head
    while cur:
        prev=cur.next
        del cur.data
        cur=prev
def count(self):
    temp=self.head
    count=0
    while(temp):
        count=+1
        temp=temp.next
    return count

i = 4
d = 4.0
s = "HackerRank"
i1=int(input(""))
d1=float(input(""))
s1="is the best place to learn and practice coding!"

sum1=i+i1
sum2=d+d1
sum3=s+s1
print(sum1)
print(sum2)
print(sum3)

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None:
    def insert(self,prev_node,new_node,position):
        if prev_node is none:
            return
            new_node=node(new_data)
            new_node.next=prev_node.next
            prev_node.next=new_node"""

            