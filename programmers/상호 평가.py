scores = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]
result = ""

for i in range(len(scores)):
    sum = 0
    cnt = 0
    tmp = []
    for j in scores:
        tmp.append(j[i])
        sum += j[i]
    for j in tmp:
        if tmp[i] == max(tmp) and j == max(tmp):
            cnt += 1
        elif tmp[i] == min(tmp) and j == min(tmp):
            cnt += 1
    if cnt == 1:
        sum -= scores[i][i]
        answer = sum/(len(scores)-1)
    else:
        answer = sum/len(scores)
    if answer >=90:
        result += "A"
    elif answer >=80:
        result += "B"
    elif answer >=70:
        result += "C"
    elif answer >=50:
        result += "D"
    else:
        result += "F"
print(result)