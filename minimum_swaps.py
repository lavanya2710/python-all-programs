"""n=int(input) 
arr = list(map(int, input().rstrip().split()))

def minimumSwaps(arr):
    temp = [0] * (len(arr) + 1)
    for pos, val in enumerate(arr):
        temp[val] = pos
        pos += 1
    swaps = 0
    for i in range(len(arr)):
        if arr[i] != i+1:
            swaps += 1
            t = arr[i]
            arr[i] = i+1
            arr[temp[i+1]] = t
            temp[t] = temp[i+1]
    return swaps

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    a = [0] * (len(arr) + 1)
    for pos, val in enumerate(arr):
        a[val] = pos
        pos += 1
    swaps = 0
    for i in range(len(arr)):
        if arr[i] != i+1:
            swaps += 1
            t = arr[i]
            arr[i] = i+1
            arr[a[i+1]] = t
            a[t] = a[i+1]
    return swaps
    

if __name__ == '__main__':
   # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    #fptr.write(str(res) + '\n')

    #fptr.close()


def swap(arr):
    a=[0]*(len(arr)+1)
    for pos,val in enumerate(arr):
        a[val]=pos
        pos=pos+1
    for i in range(len(arr)):
        if arr[i]!=i+1:
            count=count+1
            t=arr[i]
            arr[i]=i+1
            arr[a[i+1]]=t
            a[t]=a[i+1]
    return count

list=[5,4,2,1,3]
def swap(list,pos,val):
    list[pos1],list[pos2]=list[pos2],list[pos1]
    return list
list=[4,2,3,1,5]
pos1,pos2=1,3
print(swap(list,pos1-1,pos2-1))"""















