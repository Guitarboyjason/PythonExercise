n = int(input())
stairs = []
max_discount = -100000
for _ in range(n):
    stairs.append(int(input()))
    
cnt = 0
def max_score(num, stairs,cnt):
    if num == n:
        return stairs[num-1]
    if num > n:
        return max_discount
    else:
        if num ==1:
            return stairs[num-1] + max(max_score(num+1,stairs,cnt),max_score(num+2,stairs,cnt))
        if cnt == 1:
            cnt=0
            return max_score(num+2,stairs,cnt)
        else:
            return stairs[num-1] + max(max_score(num+1,stairs,cnt+1),max_score(num+2,stairs,cnt))

print(stairs)
print(max_score(1,stairs,cnt))
