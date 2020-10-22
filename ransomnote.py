def ransomnote(mag,note):
    for word in note:
        if word in mag:
            mag.remove(word)
        else:
            return False
    return True

m = int(input(""))

n = int(input(""))

mag = str(input(""))

note = str(input(""))

result=ransomnote(mag, note)
if(result):
    print("Yes")
else:
    print("No")