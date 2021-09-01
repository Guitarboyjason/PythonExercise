def num_continue(before,after):
    if before - after < 0:
        return 0
    return 1 + num_continue(after, before-after)

def print_continue(before,after):
    if before - after < 0:
        return 0
    print(before - after, end=" ")
    print_continue(after,before-after)



n = int(input())

max_count = 0
answer = -10
if n > 2:
    for i in range(int(n/2),n):
        tmp = num_continue(n,i)
        if tmp > max_count:
            max_count = tmp
            answer = i
else:
    for i in range(1,n+1):
        tmp = num_continue(n,i)
        if tmp > max_count:
            max_count = tmp
            answer = i
print(max_count)
print(n, answer,end=" ")
print_continue(n,answer)
