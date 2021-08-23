# list = [1,5,4]

# list.append(5)
# list.append(6)
# print(list)

# list.pop(0)
# print(list)
# list.pop(0)
# print(list)

n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

nodes = [[] for _ in range(n+1)]


for lines in vertex:        #인접 리스트 생성
    nodes[lines[0]].append(lines[1])
    nodes[lines[1]].append(lines[0])
print(nodes)

count = 0
node_queue = [1]        
node_remain = [i for i in range(1,n+1)]     #남은 노드들
while node_remain !=  []:
    for i in nodes[node_queue[0]]:
        if i in node_remain:
            node_queue.append(i)        #큐로 이동
            node_remain.pop(node_remain.index(i))       #remain에서 삭제
    node_queue.pop(0)
node_queue.pop(node_queue.index(1))
print(node_remain)
print(node_queue)


# run = True
# i = 0 
# while run:
#     if i == len(vertex):
#         run = False
#     else:
#         if 1 in vertex[i]:
#             vertex.pop(i)
#             i -= 1
#         i += 1
    
# print(vertex)