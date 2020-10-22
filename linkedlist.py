#inserting values
"""class node:
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
    def insert(self,prv_node,new_data):
        if prv_node is None:
            return
        new_node=node(new_data)
        new_node.next=prv_node.next
        prv_node.next=new_node
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
llist.append(1)
llist.push(10)
llist.push(2)
llist.insert(llist.head.next,50)
llist.append(11)
llist.printlist()
#deletion
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
    def deleteNode(self, key):
        temp = self.head
        if (temp is not None):  
            if (temp.data == key):  
                self.head = temp.next
                temp = None
                return
        while(temp is not None):  
            if temp.data == key:  
                break
            prev = temp  
            temp = temp.next
        if(temp == None):  
            return
        prev.next = temp.next
  
        temp = None
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data),
            temp=temp.next

llist=linkedlist()
llist.push(1)
llist.push(10)
llist.push(2)
llist.printlist()
llist.deleteNode(1)
print("\n")
llist.printlist()

#deletion with position
def delete(self,position):
    if self.head==None:
        return
    temp=self.head
    if position==0:
        self.head=temp.next
        temp=None
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

#length of linked list
def count(self):
    temp=self.head
    count=0
    while(temp):
        count+=1
        temp=temp.next
    return count

#search in linked list
def search(self,x):
    cur=self.head
    while cur!=None:
        if cur.data==x:
            return True
    cur=cur.next
    return False
if llist.search(21):
    print("yes")
else:
    print("no")




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
        temp=self.head
        if temp==None:
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
llist.push(1)
llist.push(10)
llist.push(2)
llist.printlist()
llist.delete(2)
print("\n")
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
#main
llist=linkedlist()
llist.append(4)
llist.append(5)
llist.push(2)
llist.push(1)
llist.insert(llist.head.next,3)
llist.printlist()

#delete
def delete(self,key):
    temp=self.head
    if temp is not None:
        if temp==key:
            temp=temp.next
            temp==None
            return
    while temp is not None:
        if temp==key:
            break
        prev=temp
        temp=temp.next

    if temp==None:
        return
    prev.next=temp.next
    temp=None

#delete with position
def delete(self,position):
    temp=self.head
    if temp == None:
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
        return
    next=temp.next.next
    temp.next=None
    temp.next=next

#delete linked list
def delete(self):
    temp=self.head
    while temp:
        prev=temp.next
        del temp.data
        temp=prev

#count
def count(self):
    temp=self.head
    count=0
    while temp:
        count+=1
        temp=temp.next
    return count

#search
def search(self,x):
    cur=self.head
    while cur!=None:
        if cur.data==x:
            return True
        cur=cur.next
    return False
def search(self,li,key):
    if not li:
        return False
    if li.data==key:
        return True
    return self.search(li.next,key)

def reverse(self):
    prev=None
    cur=self.head
    while cur!=None:
        next=cur.next
        cur.next=prev
        prev=cur
        cur=next        
    self.head=next"""
#doubly linked list
class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class doublylinkedlist:
    def __init__(self):
        self.head=None
    def push(self,new_data):
        new_node=node(new_data)
        new_node.next=self.head
        if self.head is not None:
            self.head.prev=new_node
        self.head=new_node

    def insertafter(self,prev_node,new_data):
        if prev_node is None:
            return 
        new_node=node(new_data)
        new_node.next=prev_node.next
        prev_node.next=new_node
        new_node.prev=prev_node
        if new_node.next is not None:
            new_node.next.prev=new_node

    def append(self,new_data):
        new_node=node(new_data)
        new_node.next=None
        if self.head is None:
            new_node.prev=None
            self.head=new_node
            return
        last=self.head
        while last.next is not None:
            last=last.next
        last.next=new_node
        new_node.prev=last
        return


    def printlist(self,node):
        while node is not None:
            print(node.data),
            #last=node
            node=node.next
        """while last is not None:
            print(last.data),
            last=last.prev"""
dlist=doublylinkedlist()
dlist.append(5)
dlist.push(2)
dlist.push(1)
dlist.append(4)
dlist.insertafter(dlist.head.next,3)
dlist.printlist(dlist.head)




















