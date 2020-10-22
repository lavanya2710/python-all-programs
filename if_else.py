""" write a code
if a num is divisible by 3 not with 5 pirnt foo
if a num is divisible by 5 not with 3 print bar
if a num is divisible by both 3 and 5 print loo

3 divisible=sum of digits/3
5 divisible=end 0,5"""

a = int(input("enter a value"))
if a % 3 == 0 and a % 5 !=0:
     print("foo")
elif a % 5 == 0 and a % 3 !=0:
    print("bar")
elif a % 3 ==0 and a % 5 ==0:
    print("loo")
else:
    print("invalid input")
