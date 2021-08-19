k = 3
num = [12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1]
links = [[-1, -1], [-1, -1], [-1, -1], [-1, -1],\
    [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], \
    [7, 4], [-1, -1], [-1, -1]]

max_k = k

# links 원소 마지막에 부모 노드를 표시해 준다
for i in range(len(links)):     
    if links[i][0:2] != [-1,-1]:
        for j in links[i][0:2]:
            if j != -1:
                links[j].append(i)
for i in range(len(links)):
    if len(links[i]) == 2:
        links[i].append(-1)     
# 부모 노드 표현 완료

# 모든 부모 노드를 탐색하여 k개로 나눠보자

def summary(num,links,parent):
    for i in links[parent][0:2]:
        if links[parent][0] != -1 and links[parent][1] != -1:
            return num[parent] + summary(num,links,links[parent][0]) + summary(num,links,links[parent][0])
        elif links[parent][0] != -1:
            return num[parent] + summary(num,links,links[parent][0])
        elif links[parent][1] != -1:
            return num[parent] + summary(num,links,links[parent][1])
        else:
            return num[parent]

max_sum = 0
def divine(num,links,k):
    global max_sum
    if k == max_k:
        max_sum = 0
    if k == 1:          #base_case
        for i in links:
            if i[2] == -1:
                if max_sum< summary(num,links,i):
                    max_sum = summary(num,links,i)
                    return max_sum
    else:
        for parent in links:
            if parent[2] != -1: # -1이 아니라는 뜻은 부모가 존재한다는 뜻
                tmp_links = links       #백업
                tmp = links.index(parent)
                print("tmp:",tmp)
                links[parent[2]][links[parent[2]].index(tmp)] = -1
                parent[2] = -1
                return min(divine(num, tmp_links,k) , divine(num,links, k-1)) # 재귀 호출

print(divine(num,links,k))
            