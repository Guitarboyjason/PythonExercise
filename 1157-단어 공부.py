word = input()
arr = [0]*26
for i in word:
    if int(ord(i)<97):
        tmp = int(ord(i))-65
    else:
        tmp = int(ord(i)) -97
    arr[tmp] += 1
cnt = 0
max_index = -1
for i in range(len(arr)):
    if cnt == 2:
        print("?")
        max_index = -1
        break;
    if max(arr) == arr[i]:
        cnt += 1
        max_index = i
if cnt != 2:
    print(chr(max_index+65))
    
