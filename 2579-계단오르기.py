n = int(input())
stairs = [0]
for _ in range(n):
    stairs.append(int(input()))
scores = [0]*(n+1)
cnt = 0
def max_score(num,cnt):
    if num == 1:
        scores[num] = stairs[num]
        return scores[num]
    else:
        if cnt == 1:
            scores[num] = stairs[num] + scores[num-2]
            return scores[num]
        else:
            if num>2:
                scores[num] = stairs + max(max_score(num-1,1),max_score(num-2,0))
                return scores[num]
            else:
                scores[num] = stairs[num] + max_score(num-1,
                
                    
print(max_score(n,cnt))
