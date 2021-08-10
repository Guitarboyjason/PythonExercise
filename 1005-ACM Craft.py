#1005 ACM Craft
def find(n) :
    return [index for index, value in enumerate(order_a) if value == n]

def answer(n):
    arr = find(n)
    arr_2 = []
    for i in len(arr):
        answer(arr[i])
        arr_2.append(structure[arr[i]])
    return max(arr_2)

T = int(input())
for i in range(T):
    N, K = map(int,input().split())
    structure = []
    order_b = []
    order_a = []
    structure.append([map(int,input().split())])
    for i in range(K):
        b,a = map(int,input().split())
        order_b.append(b)
        order_a.append(a)
    W = int(input())
    print(answer(W))
