lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
cnt_0 = 0
cnt_wins = 0
result = []

for nums in lottos:
    if nums == 0:
        cnt_0 += 1
    elif nums in win_nums:
        cnt_wins+= 1

if cnt_wins + cnt_0 == 6:
    result.append(1)
elif cnt_wins + cnt_0 == 5:
    result.append(2)
elif cnt_wins + cnt_0 == 4:
    result.append(3)
elif cnt_wins + cnt_0 == 3:
    result.append(4)
elif cnt_wins + cnt_0 == 2:
    result.append(5)
else:
    result.append(6)
    
if cnt_wins == 6:
    result.append(1)
elif cnt_wins == 5:
    result.append(2)
elif cnt_wins == 4:
    result.append(3)
elif cnt_wins == 3:
    result.append(4)
elif cnt_wins == 2:
    result.append(5)
else:
    result.append(6)
print(result)