from itertools import permutations
DIV_NUM = 10007
n = int(input())
arr = [-1]*(n+1)
def rectangle(num):
    cnt = 0
    mok = num//2
    if n//2 == 0:
        return 1
    else:
        if arr[mok] != -1:
            return arr[num]
        else:
            arr[mok] = 0
            for i in range(mok): 
                arr[mok] += len(list(permutations([i for i in  range(num-2*i)])))
         
        mok = n//2
            #print(len(permutations(num-2*i,mok))
    return cnt%DIV_NUM
print(rectangle(n))
            
