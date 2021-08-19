distance = 25
rocks = [2,14,11,21,17]
n = 2

rocks.sort()
dist_arr = []
for i in range(len(rocks)):
    if i == 0:
        dist_arr.append(rocks[i])
    elif i == len(rocks)-1:
        dist_arr.append(distance-rocks[i])
    else:
        dist_arr.append(rocks[i+1]-rocks[i])

for i in range(n):
    minimum = min(dist_arr)
    #빼면서 더해
    dist_arr[dist_arr.index(minimum)+1]+=minimum
    dist_arr = dist_arr[:dist_arr.index(minimum)] + dist_arr[dist_arr.index(minimum)+1:]
print(min(dist_arr))
print(dist_arr)

# rocks_count = rocks - n

# tmp_rocks = []
# #tmp_rocks를 포함하는 돌로 표현한다.
# #rocks는 없애는 돌로 표현
# max_distance = 0
# def substract(tmp_rocks,rocks,n):
#     global max_distance
#     if n == 0:
#         if tmp_rocks != rocks_count:
#             for i in rocks[tmp_rocks[-1]:]:
#                 tmp_rocks.append(i)
#         min = tmp_rocks[0]
#         for i in range(1,len(tmp_rocks)):
#             if tmp_rocks[i]-tmp_rocks[i-1] < min:
#                 min = tmp_rocks[i]-tmp_rocks[i-1]

#         return min
#     else:
#         for i in range(len(rocks)):
#             return max(substract(tmp_rocks+rocks[i],rocks[:i]+rocks[i+1:],n) \
#                 ,substract(tmp_rocks,rocks[:i]+rocks[i+1:],n-1))  #해당 돌을 제외함
            
#             if max_distance < substract(rocks[:i]+rocks[i+1:],n-1):
#                 max_distance = substract(rocks[:i]+rocks[i+1:],n-1)
# tmp_rocks.append(distance)
