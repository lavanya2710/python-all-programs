"""import array as arr
a=arr.array('i',[1,2,3])
for i in range(0,3):
    print(a[i])
b=arr.array('d',[1.9,2.3,7.6])
for i in range(0,3):
    print(b[i])
print(b)

import array as arr
a=arr.array("i",(1,2,3,4))
print(a)
x=10000000000000000000000000000000000000000000000
x=x+1
print(x)
print(type(x))



def leftRotate(arr, d, n): 
    for i in range(d): 
        leftRotatebyOne(arr, n) 
  
def leftRotatebyOne(arr, n): 
    temp = arr[0] 
    for i in range(n-1): 
        arr[i] = arr[i+1] 
    arr[n-1] = temp 
def printArray(arr,size): 
    for i in range(size): 
        print ("%d"% arr[i],end=" ") 
arr = [1, 2, 3, 4, 5, 6, 7] 
leftRotate(arr, 2, 7) 
printArray(arr, 7) 
  
    
def leftrot(arr,d,n):
    for i in range(d):
        leftrotbyone(arr,n)
def leftrotbyone(arr,n):
    temp=arr[0]
    for i in range(n-1):
        arr[i]=arr[i+1]
        arr[n-1]=temp
def printArray(arr,size):
    for i in range(size):
        print("%d"%arr[i],end=" ")





def leftRotate(arr, d, n): 
    for i in range(d): 
        leftRotatebyOne(arr, n) 
  
def leftRotatebyOne(arr, n): 
    temp = arr[0] 
    for i in range(n-1): 
        arr[i] = arr[i+1] 
    arr[n-1] = temp 
def printArray(arr,size): 
    for i in range(size): 
        print ("%d"% arr[i],end=" ") 
arr=input()
leftRotate=(arr,d,n)
printArray=(arr,n)


#d=rotations a=list arr
def leftrot(a,n,d):
    return a[d:]+a[:d]
n,d=map(int,input().strip().split(" "))
a=list(map(int,input().strip().split(" ")))
arr=leftrot(a,n,d)
print(*arr,sep=" ")



b_list = [0,0,0,0,0,0,0,0,0,0]
queries = [[1,5,3],[4,8,7],[6,9,1]]
for i in range(0, len(queries)):
    strt = queries[i][0]
    end = queries[i][1]
    add_1 = queries[i][2]
    length_of_b_list = len(b_list)
    for k in range (strt-1, end):
        new_value = b_list[k] + add_1
        b_list[k] = new_value
    print(b_list)
print(max(b_list))
n=10
arr=[0]*(n)
print(arr)"""
for i in range(0,5):
    for j in range(0,i+1):
        print(i)
    print("\n")
    



