#1006 습격자 초라기
def other(index,
def find(arr_1, arr_2):
    if len(arr_1) == 0 and len(arr_2) == 0:
        return 0
    max_num = max(max(arr1),max(arr2))
    cnt = 0
    if arr_1.index(max_num) == True:
        num = arr_1.index(max_num)
        cnt = 1
    else:
        num = arr_2.index(max_num)
        cnt = 2
    extra = W-max_num
    if num == 0 :
        if cnt == 1:
            max_other = max((arr_1[-1]-extra<0)?0:,arr_1[1],arr_2[0])
        else:
            max_other = max(arr_2[-1],arr_2[1],arr_1[0])
    elif num == N-1 :
        if cnt == 1:
            max_other = max(arr_1[-2],arr_1[1],arr_2[-1])
        else:
            max_other = max(arr_2[-2],arr_2[1],arr_1[-1])
    else:
        if cnt == 1:
            max_other = max(arr_1[num+1],arr_1[num-1],arr_2[num])
        else:
            max_other = max(arr_2[num+1],arr_2[num-1],arr_1[num])
    
       
T = int(input())
for _ in range(T):
    N, W = map(int,input().split())
    arr_1 = [int(x) for x in input().split()]
    arr_2 = [int(x) for x in input().split()]
        
