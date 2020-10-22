from collections import Counter
n=int(input("number of tweets"))
tweetname=[]
testcount=0
while testcount<n:
    num=int(input("enter the number of each test case:"))
    count=0
    while count<num:
        name=str(input("enter the name followed by twitter id:"))
        tweetname.append(name)
        count+=1
    testcount+=1

uniqname=[prefname.split()[0] for prefname in tweetname]
time=Counter(uniqname)
repeat=time.values()
for ele in set(repeat):
    dup=([(key,value) for key,value in sorted(time.items()) if value==ele])
    if len(dup)>1:
        for (key,value) in dup:
            print(key,value)
    maxval=max(time.values())
    tempmaxresult=[(key,value) for key,value in sorted(time.items()) if value==maxval]
    if tempmaxresult!=dup:
        for key,value in tempmaxresult:
            print(key,value)