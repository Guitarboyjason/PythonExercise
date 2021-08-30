# def Fly(gap):
#     i = 1
#     k = 1
#     l = 1
#     cnt = 0
#     tmp = 0
#     while i<= gap:
#         if cnt == l:
#             k += 1
#             if tmp == 0:
#                 tmp = 1
#             else:
#                 l += 1
#                 tmp = 0
#             cnt = 0
#         cnt += 1
#         i += 1
#     return k
# T = int(input())
# for _ in range(T):
#     x , y = map(int,input().split())
#     gap = y-x
#     print(Fly(gap))

t = int(input())

for _ in range(t):
    x, y = map(int,input().split())
    distance = y - x
    count = 0  # 이동 횟수
    move = 1  # count별 이동 가능한 거리
    move_plus = 0  # 이동한 거리의 합
    while move_plus < distance :
        count += 1
        move_plus += move  # count 수에 해당하는 move를 더함
        if count % 2 == 0 :  # count가 2의 배수일 때, 
            move += 1  
    print(count)