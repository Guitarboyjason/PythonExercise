


#greedy하게 가보자

def greedy(arr,M):
    
    for i in range(0,len(arr)):
        arr[len(arr)-i]

    if M< greedy(arr[:-1],M) +arr[-1]:

N, M = map(int,input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()


