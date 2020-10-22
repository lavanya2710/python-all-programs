"""s="mom"
    if s[0]==s[2]:
        print("same")
    else:
        print("different")
    if s[0]==s[1]:
        print("same")
    else:
        print("different")
    if s[1]==s[2]:
        print("same")
    else:
        print("different")"""


def fib(n):
    a=0
    b=1
for i in range(2,n):
    c=a+b
    a=b
    b=c
    print(c)
fib(10)
