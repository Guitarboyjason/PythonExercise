def find_path(path, now_node, remain_dist, items):
    max_items = 0
    if remain_dist == 0:
        return 0
    for i in path:
        if i[0] == now_node and i[2] <= remain_dist:
            tmp_item = items[i[1]-1] + find_path(path, i[1]-1, remain_dist-i[2], items)
            if tmp_item > max_items:
                max_items = tmp_item
        elif i[1] == now_node and i[2] <= remain_dist:
            tmp_item = items[i[0]-1] + find_path(path, i[0]-1, remain_dist-i[2], items)
            if tmp_item > max_items:
                max_items = tmp_item
    if max_items == 0:
        return 0
    return max_items
    


n,m,r = map(int, input().split())
t = [int(x) for x in input().split()]

path = []
for i in range(r):
    path.append([int(x) for x in input().split()])

max_items = 0
for first_node in range(1,n+1):
    item_sum = find_path(path, first_node, m, t)
    if item_sum > max_items:
        max_items = item_sum
print(max_items)
