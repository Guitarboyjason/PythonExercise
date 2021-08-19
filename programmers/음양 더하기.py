absolutes = [4,7,12]
signs = [True,False,True]
sum = 0

for i in range(len(absolutes)):
    if signs[i] == True:
        sum += absolutes[i]
    else:
        sum -= absolutes[i]
print(sum)