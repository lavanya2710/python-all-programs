def arraymanuplulation(n,queries):
    arr=[0]*(n)
    for i in range(0, len(queries)):
        strt = queries[i][0]
        end = queries[i][1]
        add_1 = queries[i][2]
        for k in range (strt-1, end):
            new_value = arr[k] + add_1
            arr[k] = new_value
    return(max(arr))
    
def arraymanuplulation(n,queries):
    arr=[0]*(n)
    for qls in queries:
        for i in range(qls[0],qls[1]):
            result[i]+=qls[2]
        print(max(result[i]))