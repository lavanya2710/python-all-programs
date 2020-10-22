#through list
"""stack1=[]
stack1.append("a")
stack1.append("b")
stack1.append("c")
print(stack1)
print(stack1.pop())
print(stack1.pop())
print(stack1.pop())
print(stack1)
#through deques
from collections import deque
stack1=[]
stack1.append("a")
stack1.append("b")
stack1.append("c")
print(stack1)
print(stack1.pop())
print(stack1.pop())
print(stack1)
print(stack1.pop())
print(stack1)
#through queue
from queue import LifoQueue
stack1=LifoQueue(maxsize=3)
print(stack1.empty())
print(stack1.qsize())

def createstack():
    stack=[]
    return stack
def size(stack):
    return len(stack)
def isempty(stack):
    if size(stack)==0:
        return True
def push(stack,item):
    stack.append(item)
def pop(stack):
    if isempty(stack):
        return 
    return stack.pop()
def reverse(string):
    n=len(string)
    stack=createstack()
    for i in range(0,n,1):
        push(stack,string[i])
    string=""
    for i in range(0,n,1):
        string+=pop(stack)
    return string
string="lavanya"
string=reverse(string)
print(string)

def reverse(string):
    string=string[::-1]
    return string
string="hello"
string=reverse(string)
print(string)
stack=[]

    def push(self,item):
        stack.append(item)
        return
    def pop(self):
        if not stack:
            return stack is empty
        else:
            e=stack.pop()
            return e
import collections
stack=collections.deque()
print(stack)
stack.append(10)
stack.append(20)
stack.append(30)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(not stack)
import queue
stack=queue.LifoQueue(maxsize=3)
stack.put(10)
stack.put(20)
stack.put(30)
print(stack.get())
print(stack.get())
print(stack.get())
queue=[]
def enqueue():
    queue.append(10)
    print(queue)
def deque():
    if not deque:
        return 
    else:
        b=queue.pop(0)
        print(b)
def display():
    print(queue)
obj=enqueue()
print(obj)
obj1=deque()
print(obj1)
obj2=display()
print(obj2)"""

import queue
q=queue.Queue()
q.put(10)
q.put(20)
q.put(30)
print(q)
print(q.get())
