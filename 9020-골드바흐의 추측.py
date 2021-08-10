#9020 골드바흐의 추측


def eratostenes(n):
    arr= [i for i in range(2,n+1)]
    for i in arr:
        if i != -1:
            for j in arr[i-1:]:
                if j != -1:
                    if j%i == 0:
                        arr[j-2] = -1
    return arr
            
def goldbach(n):
    arr = eratostenes(n)
    tmp_i = 0
    tmp_j = 0
    for i in arr[int(n/2):0:-1]:
        if i != -1:
            for j in arr[int(n/2)+1:]:
                if j!= -1:
                    if i+j == n:
                        tmp_i = i
                        tmp_j = j
    print(tmp_i,tmp_j)

T = int(input())
for i in range(T):
    n = int(input())
    goldbach(n)
