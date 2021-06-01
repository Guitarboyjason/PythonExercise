N = int(input())

def gcd(x,y):
    mod = x%y
    while mod>0:
        x = y
        y = mod
        mod = x%y
    return y
arr_num  = []
for _ in range(N):
    arr_num.append(int(input()))
min_num = 1000000000
for i in range(N-1):
    for j in range(i+1,N):
        if min_num> abs(arr_num[i] - arr_num[j]):
            min_num = abs(arr_num[i]-arr_num[j])
for i in range(2,min_num+1):
    if min_num%i == 0:
        print(i,end=' ')
