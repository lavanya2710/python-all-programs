# Python program to illustrate 
# enumerate function in loops 
l1 = ["eat","sleep","repeat"] 
  
# printing the tuples in object directly 
for ele in enumerate(l1): 
    print(ele) 

# changing index and printing separately 
for count,ele in enumerate(l1): 
     if count == 2:
         print('2:', ele)