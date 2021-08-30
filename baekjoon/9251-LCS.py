#9251 LCS

#case 1 2 3 이 있다.
def LCS(case,str1,str2):
    if len(str1) == 0 or len(str2) == 0:
        return 0
    if case==1:
        if arr[len(str1)-1] == -1:
            cnt = 0
            for i in str2[::-1]:
                cnt +=1
                if i == str1[-1]:
                    arr[len(str1)-1] = 1+max(LCS(1,str1,str2[0:-cnt]),LCS(2,str1,str2[0:-cnt]),LCS(3,str1,str2[0:-cnt]))
                    return arr[len(str1)-1]
            return 0
        else:
            return arr[len(str1)-1]
    elif case == 2:
        cnt = 0
        for i in str1[::-1]:
            cnt += 1
            if i == str2[-1]:
                return 1+ max(LCS(1,str1[0:-cnt],str2),LCS(2,str1[0:-cnt],str2),LCS(3,str1[0:-cnt],str2))
        return 0
    else:
        return max(LCS(1,str1[0:-1],str2[0:-1]),LCS(2,str1[0:-1],str2[0:-1]),LCS(3,str1[0:-1],str2[0:-1]))
str1 = input()
str2 = input()
arr = [-1]*len(str1)
print(max(LCS(1,str1,str2),LCS(2,str1,str2),LCS(3,str1,str2)))
