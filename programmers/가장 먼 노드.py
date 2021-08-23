n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

level_arr = [-1 for i in range(n)]
print(level_arr)
level_arr[0] = 0
level = 1

# for i in vertex:
#     for j in level_arr:
#         if j == level:
            
#             # if i.index(1) == 0:
#             #     arr[i[0]-1] = 1
#             # else:
#             #     arr[i[1]-1] = 1
# while -1 in level_arr:
#     for i in level_arr:
#         if i != -1:
#             for j in vertex:
#                 if j != -1:
#                     if level_arr.index(i)+1 in j:
#                         if j.index(level_arr.index(i)+1) == 0:
#                             if level_arr[j[1]-1] == -1:
#                                 level_arr[j[1]-1] = level
#                         else:
#                             if level_arr[j[0]-1] == -1:
#                                 level_arr[j[0]-1] = level
#                         vertex[vertex.index(j)] = -1
#         level += 1


  #재귀적으로 해결해보자

def longgest_node(node, level, level_arr):
    if -1 not in level_arr:
        

print(level_arr)
cnt = 1
max_count = 0
for i in level_arr:
    if max_count == i:
        cnt += 1
    elif max_count < i:
        max_count = i
        cnt = 1
print(max_count)