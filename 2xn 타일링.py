import math
DIV_NUM = 10007
n = int(input())

def rectangle(num):
    cnt = 0
    if n//2 == 0:
        return 1
    else:
        mok = n//2
        for i in range(mok):
            math.comb(num-2*i,mok)
