price = 3
money = 20
count = 4

sum  = 0
for i in range(1,count+1):
    sum += i
if sum * price <= money:
    print(0)
else:
    print(sum*price - money)
