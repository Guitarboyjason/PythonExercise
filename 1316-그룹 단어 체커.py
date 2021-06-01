arr = []
cnt = 0
def finder(word):
    if len(arr) == 0:
        arr.append(word[0])
        return(finder(word[1:]))
    if len(word) == 1 :
        if word == arr[-1]:
            return 1
        elif word not in arr:
            return 1
        else:
            return 0
    elif word[0] not in arr:
        arr.append(word[0])
        return(finder(word[1:]))
    elif word[0] == arr[-1]:
        return(finder(word[1:]))
    
    else:
        return 0

n = int(input())
sum = 0
for _ in range(n):
    word = input()
    print(word[-1])
    print(finder(word))
    sum+= finder(word)
print(sum)

        
