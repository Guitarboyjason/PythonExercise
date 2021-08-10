from queue import LifoQueue

N = int(input())

def hanoi(stack_1,stack_2,stack_3):
    if stack_3.size == N:
        return 1
    if stack_1 != 

stack_1 = LifoQueue(maxsize = N)
stack_2 = LifoQueue(maxsize = N)
stack_3 = LifoQueue(maxsize = N)

for i in range(N,0,-1):
    arr_1.append(i)