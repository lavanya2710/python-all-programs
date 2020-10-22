#selection
list=['t','u','t','o','r','i','a','l']
for i in range(len(list)):
    min_val=min(list[i:])
    min_index=list.index(min_val)
    list[i],list[min_index]=list[min_index],list[i]
print(list)
"""
#bubble sort
list=[5,3,4,1,2]
for j in range(len(list)-1):
    for i in range(len(list)-1):
        if list[i]>list[i+1]:
            list[i],list[i+1]=list[i+1],list[i]
print(list)
#insertion
def insertion(list):
    for i in range(1,len(list)):
        cur=list[i]
        pos=i
        while cur<list[pos-1] and pos>0:
            list[pos]=list[pos-1]
            pos=pos-1
        list[pos]=cur
list1=[5,3,4,1,2]
insertion(list1)
print(list1)
#merge sort
def mergeSort(arr): 
	if len(arr) >1: 
		mid = len(arr)//2 
		L = arr[:mid] 
		R = arr[mid:] 

		mergeSort(L) 
		mergeSort(R) 

		i = j = k = 0
		
		
		while i < len(L) and j < len(R): 
			if L[i] < R[j]: 
				arr[k] = L[i] 
				i+= 1
			else: 
				arr[k] = R[j] 
				j+= 1
			k+= 1
		
		while i < len(L): 
			arr[k] = L[i] 
			i+= 1
			k+= 1
		
		while j < len(R): 
			arr[k] = R[j] 
			j+= 1
			k+= 1

def printList(arr): 
	for i in range(len(arr)):		 
		print(arr[i]) 
	print() 

if __name__ == '__main__': 
	arr = [12, 11, 13, 5, 6, 7] 
	#printList(arr) 
	mergeSort(arr) 
	printList(arr) 

#quick sort
def pivot_place(list,first,last):
    pivot=list[first]
    left=first+1
    right=last
    while True:
        while left<=right and list[left]<=pivot:
            left=left+1
        while left<=right and list[right]>=pivot:
            right=right-1
        if right<left:
            break
        else:
            list[left],list[right]=list[right],list[left]
    list[first],list[right]=list[right],list[first] 
    return right
def quick(list,first,last):
    if first<last:
        p=pivot_place(list,first,last)
        quick(list,first,p-1)
        quick(list,p+1,last)
#main
list=[5,3,4,2,1]
n=len(list)
quick(list,0,n-1)
print(list)"""