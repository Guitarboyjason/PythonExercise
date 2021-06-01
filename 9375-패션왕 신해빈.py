import math

tstCase = int(input())
t_list = {}
sort_list = set([])
for _ in range(tstCase):
    n = int(input())
    for i in range(n):
        name,sort = input().split()
        t_list[name] = sort
        sort_list.add(sort)
    sum = 0
    for i in range(1,len(sort_list)+1):
        cnt = 0
        if sort_list[
        sum+= math.comb(n,i)
        print(sum)
    print(sum)
