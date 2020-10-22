"""dict={"alpha":[20,30,40],"beta":[30,50,70]}
for key,value in dict.items():
    print(value)
    avr=(value[0]+value[1]+value[2])/3
    print(avr)

s="hello world"
print(s.capitalize())

arr=[1,2,9,4,5]
arr1=arr[:]
arr1.sort()
if arr1==arr:
    print("1")
else:
    print("0")

arr = ['t','u','t','o','r','i','a','l']
for i in range(len(arr)):
    min_val=min(arr[i:])
    min_index=arr.index(min_val)
    arr[i],arr[min_index]=arr[min_index],arr[i]
print(arr)

list=[]
list1=[1,2,3,4,5]
list.append(list1)
print(list)
list.remove(2)

a1=[1,2,3,4,"a","b","a","b"]
print(a1.count(3))

a=5
b=2
temp=a
a=b
b=temp
print(a)
print(b)

list=[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]
print(list.index(5))

#linked list
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
    def insert(self,prev_node,new_data):
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
llist.push(1)
llist.push(2)
llist.insert(llist.head.next,3)
llist.append(4)
llist.printlist

def delete(self,key):
    temp=self.head
    if temp is not None:
        if temp.data==key:
            self.head=temp.next
            temp=None
            return
            
    while temp is not None:
        if temp.data==key:
            break
        prev=temp
        temp=temp.next
    if temp==None:
        return
    prev.next=temp.next
    temp=None
def printlist():
    temp=self.head
    while(temp):
        print(temp.data),
        temp=temp.next
#delete with position
def delete(self,pos):
    temp=self.head
    if temp ==None:
        return
    if pos==0:
        temp=temp.next
        temp=None
        return
    for i in range(pos-1):
        temp=temp.next
        if temp is None:
            break
    if temp is None:
        return
    if temp.next is None:
        return
    next=temp.next.next
    temp=None
    temp.next=next

list=[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]
print(list.index(5))

list=[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]
ele=5
pos=-1
for i in range(len(list)-1):
    if list[i]==ele:
        pos=i
        break
if pos>-1:
    print(pos)
else:
    print(pos)

list=[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]
ele=5
pos=len(list)-list[::-1].index(ele)-1
print(pos)

def index(list,ele):
    indexpos=[]
    for i in range(len(list)):
        if list[i]==ele:
            indexpos.append(i)
    return indexpos
list=[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]
indexpos=index(list,5)
print(indexpos)

list=[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]
index=[i for i in range(len(list)) if list[i] ==5 ]
print(index)"""

