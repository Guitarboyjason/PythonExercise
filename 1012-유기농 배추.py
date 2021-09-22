
def Find_path(x,y):
    if arr[x][y] == 1:
        arr[x][y] = 0
        if x == M-1 and y == N-1:
            
        elif x == M-1 :

        elif y == N-1:

        if x == 0 and y == 0:
            Find_path(x,y+1)        
            Find_path(x+1,y)
        elif x == 0:
            Find_path(x,y-1) 
            Find_path(x,y+1)        
        elif y == 0:
            Find_path(x-1,y) 
            Find_path(x+1,y)
        else:  
            Find_path(x-1,y) 
            Find_path(x+1,y) 
            Find_path(x,y-1) 
            Find_path(x,y+1)

T = int(input())
global M,N,K
for _ in range(T):
    M,N,K = map(int,input().split())
    arr = [[0 for __ in range(M)] for ___ in range(N)]
    for i in range(K):
        X,Y = map(int, input().split())
        arr[Y][X] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                Find_path(j,i)
                cnt += 1

    print(arr)
    print(cnt)
