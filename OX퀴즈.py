n = int(input())
for _ in range(n):
    correct = input()
    cnt =0
    sum = 0
    for i in correct:
        if i == 'O':
            cnt+= 1
            sum += cnt
        else:
            cnt = 0
    print(sum)
