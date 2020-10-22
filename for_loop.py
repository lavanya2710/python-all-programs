
"""for i in range(0,11,2):
    print(i)
#strings
a=("geeksforgeeks")
print(a)
#string indexing
print(a[0])
print(a[1])
print(a[-4])
#string slicing

a=("bytes of python")
print("a")
print(a[2:10])

a=("bytes of python")
print("a")
print(a[2:-1])

a1=("lavanya")
print(a1)
a1=("love")
print(a1)
#format strings
a = "{} {} {}".format("geeks","for","geeks")
print(a)
a="{2} {0} {1}".format("hello","world","hai")
print(a)
a="{lyf} {live} {long}".format(lyf="hello",live="world",long="hai")
print(a)

a="{:<10} {:^10} {:>10}".format("geeks" ,"for", "geeks")
print(a)

a="geeks"
a="a" +" for" + "geeks"
print (a)

a="hello"
b="world"
print(id(a))
print(id(b))


a="hello"
print(a)
a+="world"
print(a)
print(id(a))

a= '''i'am good'''
print(a)

str = "geeksforgeeks is for geeks
str2 = "geeks"
print (str.find( str2, 4) ) 
print ( str.rfind( str2, 4) ) 

a="hello hello hello again hello"
b="hello"
print(a.find(b,4))
print(a.rfind(b,4))

a="hello world hello world again"
b="hello"
if b.startswith(a):
    print(a)
else:
    print(a)
if b.endswith(a):
    print(a)
else:
    print(a)


a="hello"
b="world"
if a.isupper():
    print("correct")
else:
    print("use upper")
if b.islower():
    print("corect")
else:
    print("lower case")

a="hello"
print(a.upper())

b="WORLD"
print(b.lower())

c="hElLo"
print(c.lower())

d="HeLlo wORlD"
print(d.swapcase())"""

e="hello world this is lavanya"
print(e.title())"""

b="geeks for geeks"
def convert(string):
    a=list(string.splits(" "))
return a
