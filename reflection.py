def reverse(seq):
    seqtype=type(seq)
    emptyseq=seqtype()
    if seq==emptyseq:
        return emptyseq
    restrev=reverse(seq[1:])
    first=seq[0:1]
    result=restrev+first
    return result
print(reverse("hello"))
print([1,8,2,3,4,5])


