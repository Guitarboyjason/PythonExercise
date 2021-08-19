s = "aabbaccc"
answer = ""
for i in range(1,int(s/2)+1):
    copy = s[:i]
    tmp = s[i:]
    count = 1
    min = len(s)
    while tmp != "":
        if copy == tmp[:i]:
            count += 1
        else:
            answer += str(count)+copy
            
