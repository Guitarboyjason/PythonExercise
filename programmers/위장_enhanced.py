clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

clothes.sort(key = lambda x : x[1])
print(clothes)

sum = 1
count = 1

for i in range(len(clothes)):
    if i != len(clothes)-1 and clothes[i][1] == clothes[i+1][1]:
        count += 1
    else:
        sum *= (count+1)
        count = 1
print(sum-1)