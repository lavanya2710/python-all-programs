# def print_r(i):
#     if i <=-100:
#         return 0
#     print(i)
#     print_r(i-1)

# print_r(10)



def merge_sort(ls):
    if len(ls) >= 2:
        mid=len(ls)//2
        l=ls[:mid]
        r=ls[mid:]
        merge_sort(l)
        merge_sort(r)
    