clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

def solution(clothes):
    # print(clothes)
    clothes.sort(key=lambda x:(x[1]))   #종류에 따라 정렬
    # print(clothes)
    arr = []
    cnt = 1
    tmp = clothes[0][1]
    for i in clothes:
        cnt += 1
        if i[1] != tmp or i == clothes[-1]:
            arr.append(cnt)
            cnt = 1
            tmp = i[1]
    # print(arr)
    result = 1
    for i in arr:
        result = result * i
    # print(result)
    return result-1
    # arr = [[]for _ in range(30)]
    # tmp = clothes[0][1]
    # cnt = 0
    # for i in clothes:
    #     if i[1] != tmp:
    #         cnt += 1
    #         tmp = i[1]
    #     else :
    #         arr[cnt].append(i)
    # for i in range(len(arr)):
    #     if arr[i] == []:
    #         arr = arr[:i]
    #         break
    # return len(arr[0])*(solution(arr[1:]))

# def easier_arr(clothes):
#     clothes.sort(key=lambda x:(x[1]))
#     print(clothes)    
print(solution(clothes))