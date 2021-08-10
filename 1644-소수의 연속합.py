#1644 소수의 연속합
#일단 소수의 배열을 먼저 구해야하나

def primeNum(N):
    prime = [True]*(N+1)

    m = int(N **0.5)
    for i in range(2,m+1):
        if prime[i]==True:
            for j in range(i+i,N+1,i):
                prime[j] = False
    return [i for i in range(2,N+1) if prime[i] == True]

N = int(input())
arr = primeNum(N)
def contiSum(true_false,summary,arr,N):
    if summary>N:
        return 0
    elif summary == N:
        return 1
    if len(arr)== 1:
        if summary+arr[0] == N:
            return 1
        else:
            return 0
    if true_false == 1:
        return contiSum(1,summary+arr[-1],arr[:-1],N)
    else:
        return contiSum(1,summary+arr[-1],arr[:-1],N) + contiSum(0,summary,arr[:-1],N)
print(contiSum(0,0,arr,N))
