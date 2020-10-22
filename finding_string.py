"""a="lavanya"
for i in a:
    print(i)"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
"""def repeatedString(s, n):
    s=input()
    n=input()
    c = s.count("a")
    div=n//len(s)
    i=n%len(s)
    if i==0:
        c= c*div
    else:
        m = n%len(s)
        c= c*div+s[:m].count('a')
    return c
    
s=input()
n=int(input())
c=s.count("a")
l=n//len(s)
i=n%len(s)
if i==1:
    c=c*l
else:
    mod=n%len(s)
    c=c*l+s[:mod].count("a")
    print(c)

s, n = input().strip(), int(input().strip())
print(s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))"""







