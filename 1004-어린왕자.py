#1004 어린왕자

T = int(input())
for i in range(T):
    x1,y1,x2,y2 = map(int,input().split())
    cnt = 0
    n = int(input())
    for i in range(n):
        x,y,r =  map(int,input().split())
        if (x-x1)**2 + (y-y1)**2 < r**2:
            cnt +=1
        if (x-x2)**2 + (y-y2)**2 < r**2:
            cnt +=1
        if ((x-x1)**2 + (y-y1)**2 < r**2) and ((x-x2)**2 + (y-y2)**2 < r**2):
            cnt -=2
    print(cnt)    

    
