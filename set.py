"""a=set()
print(a)
a=set("geeksforgeeks")
print(a)
a="geeksforgeeks"
b=set(a)
print(b)
a=set([1,2,3,4])
print(a)
a=set([1,2,2,4,3,4,4,4,4,5,6,6,7,8,8,9,9,7,6,5,4,3,3])
print(a)
a=set(["geeks",1,8,"for"])
print(a)ss
a=set("geeks")
a.add(4)
a.add(8)
a.add("for")
print(a)
a=set(["geeks",1,8,"for"])
for i in range(1,6,2):
    a.add(i)
print(a)
a=set(["geeks",1,8,"for"])
a.update([6,7])
print(a)
a=set(["geeks","for", "geeks"])
print(a)
for i in a:
    print(i,end=" ")
print("for" in a)

a=set([1,2,3,4,5,6,7,8,9])
a.discard(33)
print(a)

a=set([1,2,3,4,5,6,7,8,9])
for i in range(1,6):
    a.discard(i)
print(a)

a=set([1,2,3,4,5,6,7,8,9])
a.pop()
print(a)

a=[1,2,3,4,5,6,7,8,9]
a.pop()
print(a)
a=set([1,2,3,4,5,6,7,8,9,5,4,4,3])
a.clear()
print(a)
a=("g","e","e","k","f","o","r")
b=frozenset(a)
print(b)
print(frozenset())
a=set([1,2,3,4,5,6,7,8,9,5,4,4,3])
a.remove(3)
print(a)
a=set([1,2,3,4,5,6,7,8,9,55,4,4,3])
b=set([1,2,3,4,5,6,7])
a.issubset(b)
print(a)

bri=set(["india","usa","israel"])
print(bri)
print("india" in bri)
print("china" in  bri)
bric=bri.copy()
print(bric)
bric.add("china")
print(bric)
bric.remove("usa")
print(bric)
bric.issuperset(bri)
print(bric & bri)
print(bric| bri)"""

















