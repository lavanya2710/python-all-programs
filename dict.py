"""a={1:"geeks",2:"for",3:[1,2,3]}
print(type(a))
print(a)
a=dict({1:"geeks",2:[1,2,3],3:"geeks"})
print(a)
a=([(1,"geeks"),(2,"for"),(3,"geeks")])
print(a)
#nested dictionary
dict={1:"geeks",2:"for",3:{"a":"welcome","b":"to","c":"geeks"}}
print(dict)
a={}
a[0]="geeks"
a[1]="for"
a[2]=1
print(a)
a['set']=2,3,4
print(a)
#updating a new value
a[2]=4
print(a)
#nested dictionary
a[4]={"nested":{1:"geeks",2:"for",3:"geeks"}}
print(a)

a={1:"geeks",2:"for",3:"geeks"}
print(a[2])
#get()
a={1:"geeks",2:"for",3:"geeks"}
print(a.get(3))

a={"nest":{1:"geeks",2:"for",3:"geeks"},
   "tested":{"A":"welcome","B":"to","c":"geeks"}}
del a["nest"][2]
print(a)
#popitem
a= {1: 'Geeks', 'name': 'For', 3: 'Geeks'} 
b=a.popitem()
print(a)
dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'} 
dict.clear()
print(dict)

ab={"lavanya":8360,
    "love":8470,
    "pogo":8590,
    "ananaya":8699}
print(ab)
print("the length of ab is {}".format(len(ab)))
print(ab["love"])
del ab["ananaya"]
for name,num in ab.items():
   print("{} and {}".format(name,num))
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print("\nGuido's address is", ab['Guido'])


ab["rara"]=9872
if "rara" in ab:
   print(ab["rara"])"""


"""n=int(input(" "))
for i in range(1,n+1):
   print(i,end="")

d=dict()
d["abc"]=123
d["xyz"]=345
for i in d:
   print("%s %d"%(i,d[i]))

for i in range(1,5):
   for j in range(i):
      print(i,end="")
   print()

for i in "geeksforgeeks":
   if i=="e" or i=="s":
      break
   print(i)

for i in "geeksforgeeks":
   pass
print(i)

s="geeksforgeeks"
for i in reversed(s):
   print(i,end=" ")"""

list=[1,2,30,4,4,4,4,4,5,5,5]
for i in sorted (set(list)):
   print(i,end=" ")










