list= ["c=","c-","dz=","d-","lj","nj","s=","z="]
word = input()
cnt = 0
i = 0
while i < len(word):
    if i == len(word)-1:
        i+=1
        cnt+=1
    elif word[i:i+2] in list or word[i:i+2] == "dz":
        if word[i:i+2] == "dz" and i!= len(word)-2 and word[i:i+3] == list[2]:
            cnt+=1
            i+=3
        else:
            cnt+=1
            i += 2
            
    else:
        i += 1
        cnt +=1
print(cnt)
