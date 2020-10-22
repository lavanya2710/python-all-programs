#linear
"""def search(list,key):
    list1=[]
    flag=False
    for i in range(len(list)):
        if key==list[i]:
            flag=True
            list1.append(i)
    if flag==True:
        print("key found",i)
        for i in list1:
            print(i)
    else:
        print("not found")
list=[5, 6, 7, 8, 9, 10, 1, 2, 3]
key=int(input("enter key value"))
search(list,key)
#binary search
def binary(list,key):
    low=0
    high=len(list)-1
    
    found=False
    while low<=high and not found:
        mid=low+(high-2)//2
        if key==list[mid]:
            found=True
        elif key>=list[mid]:
            low=mid+1
        else:
            high=mid-1
    if found==True:
        print("key found")
    else:
        print("not found")
list=[4,6,8,1,3,9,10]
list.sort()
key=int(input("enter key value"))
binary(list,key)

#exponential search
def binarySearch(list,key):
    low=0
    high=len(list)-1
    found=False
    mid=(low+high)//2
    while low<=high and not found:
        if key==list[mid]:
            found=True
        elif key>list[mid]:
            low=mid+1
        else:
            high=mid-1
list=[5,3,4,1,2]
key=int(input("enter key value"))
binarySearch(list,key)"""

