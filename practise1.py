"""arr=[1,5,4,3,2]
for i in range(len(arr)):
    min_val=min(arr[i:])
    min_index=arr.index(min_val)
    arr[i],arr[min_index]=arr[min_index],arr[i]
print(arr)

arr=[1,5,4,3,2]
for j in range(len(arr)-1):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
print(arr)

def insertion(arr):
    for i in range(1,len(arr)):
        cur=arr[i]
        pos=i
        while cur<arr[pos-1] and pos>0:
            arr[pos]=arr[pos-1]
            pos=pos-1
        arr[pos]=cur
arr=[1,5,4,3,2]
insertion(arr)
print(arr)

#merge sort
def mergesort(arr):
    if len(arr)==1:
        return arr
    if len(arr)>1:
        mid=len(arr)//2
        left_arr=arr[:mid]
        right_arr=arr[mid:]
        mergesort(left_arr)
        mergesort(right_arr)
        i=j=k=0
        while i<len(left_arr) and j<len(right_arr):
            if left_arr[i]<right_arr[j]:
                arr[k]=left_arr[i]
                i=i+1
                k=k+1
            else:
                arr[k]=right_arr[j]
                j=j+1
                k=k+1
        while i<len(left_arr):
            arr[k]=left_arr[i]
            i=i+1
            k=k+1
        while j<len(right_arr):
            arr[k]=right_arr[j]
            j=j+1
            k=k+1
#arr=[1,5,4,3,2]
arr=[4]
mergesort(arr)
print(arr)

#quick sort
def pivot_place(arr,first,last):
    pivot=arr[first]
    left=first+1
    right=last
    while True:
        while left<=right and arr[left]<=pivot:
            left=left+1
        while left<=right and arr[right]>=pivot:
            right=right-1
        if left>right:
            break
        else:
            arr[left],arr[right]=arr[right],arr[left]
    arr[first],arr[right]=arr[right],arr[first]
    return right
def quick(arr,first,last):
    if first<last:
        p=pivot_place(arr,first,last)
        quick(arr,first,p-1)
        quick(arr,p+1,last)
arr=[1,5,4,3,2]
n=len(arr)
quick(arr,0,n-1)
print(arr)

#linear search
def linear(list,key):
    list1=[]
    flag=False
    for i in range(len(list)):
        if key==list[i]:
            flag=True
            list1.append(i)
    if flag==True:
        print("found",i)
    else:
        print("not found")
list=[1,2,3,4,5]
key=int(input("enter a key"))
linear(list,key)

def binary(list,key):
    low=0
    high=len(list)
    found=False
    while low<=high and not found:
        mid=(low+high)//2
        if key==list[mid]:
            found=True
        elif key>list[mid]:
            low=mid+1
        else:
            high=mid-1
    if found==True:
        print("found")
    else:
        print("not found")
list=[345,455,356,976,34567,2456789]
key=int(input("enter a key"))
list.sort()
binary(list,key)

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
        last=self.head
        while(last.next):
            last=last.next
        last.next=new_node
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data),
            temp=temp.next

llist=linkedlist()
llist.append(5)
llist.push(2)
llist.push(1)
llist.append(4)
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

    def delete(self):
        if self.head is None:
            return
        else:
            self.head=self.head.next

    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data),
            temp=temp.next
llist=linkedlist()
llist.push(2)
llist.push(1)
llist.delete()
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

    def delete(self):
        if self.head is None:
            return
        else:
            temp=self.head
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None

    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data),
            temp=temp.next
llist=linkedlist()
llist.push(2)
llist.push(1)
llist.delete()
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

    def delete(self,position):
        if self.head is None:
            return
        temp=self.head
        if position==0:
            self.head=self.head.next.next
            self.head=None
            return
        for i in range(position-1):
            temp=temp.next
            if temp is None:
                break
        if temp is None:
            return 
        if temp.next is None:
            return 
        next=temp.next.next
        temp.next=None
        temp.next=next
        
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data),
            temp=temp.next
llist=linkedlist()
llist.push(2)
llist.push(1)
llist.delete(1)
llist.printlist()

s="hacker"
n=len(s)
even=""
odd=""
for i in range(0,n):
    if i%2==0:
        even+=s[i]
    if i%2==1:
        odd+=s[i]
print(even+" "+odd)

arr=[4,3,2,1]
print(arr[::-1])

strings=[1,2,3,4,5,1,2,3]
queries=[1,2,3,6]
qdict={}
result=[]
for q in queries:
    qdict[q]=0
for s in strings:
    if s in qdict:
        qdict[s]+=1
for q in queries:
    result.append(qdict[q])
print(result)

#fib
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
fib(5)
#fac
def fac(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
m=fac(5)
print(m)
#prime or not
num=14
if num<=1:
    print("invalid")
for i in range(2,num):
    if num%i==0:
        print("not prime")
        break
    else:
        print("prime")
        break

#recur fib
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
m=fib(4)
print(m)
#rec fact
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
m=fact(5)
print(m)

class Node:
    def __init__(self,value):
        self.left=None
        self.data=value
        self.right=None
class Tree:
    def createnode(self,data):
        return Node(data)
    def insert(self,node,data):
        if node is None:
            return self.createnode(data)
        if data<node.data:
            node.left=self.insert(node.left,data)
        else:
            node.right=self.insert(node.right,data)
        return node
    def traverse_inorder(self,root):
        if root is not None:
            self.traverse_inorder(root.left)
            print(root.data)
            self.traverse_inorder(root.right)
    def delete(root,key):
        if root==None:
            return None
        if root.left==None and root.right==None:
            if root.key==key:
                return None
            else:
                return root
        key_node=None
        q=[]
        q.append(root)
        while(len(q)):
            temp=q.pop(0)
            if temp.data==key:
                key_node=temp
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        if key_node:
            x=temp.data
            key_node.data=x
        return root

#main
tree=Tree()
root=tree.createnode(2)
tree.insert(root,5)
tree.insert(root,7)
tree.insert(root,10)
tree.insert(root,25)
tree.insert(root,20)
tree.insert(root,12)
tree.insert(root,30)
tree.insert(root,3)
tree.traverse_inorder(root)
key=10
root=delete(root,key)
tree.traverse_inorder(root)"""

n=5
k=20
arr=[10,20,30,40,50]
arr=set(arr)
print(arr)
c=0
for i in arr:
    if i+k in arr:
        print(i+k)
        c=c+1

while True:
    if root.info>v1 and root.info>v2:
        return root=root.left
    elif root.info<v1 and root.info<v2:
        return root=root.right
    else:
        break
    return 