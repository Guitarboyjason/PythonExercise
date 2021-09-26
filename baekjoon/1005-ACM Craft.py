# #1005 ACM Craft
# def find(n) :
#     return [index for index, value in enumerate(order_a) if value == n]

# def answer(n):
#     arr = find(n)
#     arr_2 = []
#     for i in len(arr):
#         answer(arr[i])
#         arr_2.append(structure[arr[i]])
#     return max(arr_2)

# T = int(input())
# for i in range(T):
#     N, K = map(int,input().split())
#     structure = []
#     order_b = []
#     order_a = []
#     structure.append([map(int,input().split())])
#     for i in range(K):
#         b,a = map(int,input().split())
#         order_b.append(b)
#         order_a.append(a)
#     W = int(input())
#     print(answer(W))


#=============================================================
#09.26

# def find_path(W):
#     for i in range(len(K)):
#         if rules[K][1] == W:


T = int(input())
for i in range(T):
    N,K = map(int,input().split())
    delay_arr = [int(i) for i in input().split()]
    print(delay_arr)
    rules = [[int(i) for i in input().split()] for i in range(K)]
    W = int(input())
    # for j in range(len(rules)):


