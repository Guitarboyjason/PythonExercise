nums =  [1,2,3,4]
arr = []
result = 0

def getit(nums, count):
    global arr
    global result
    for i in range(len(nums)):
        if count == 0 :
            if primeNum(sum(arr)):
                result +=  1
                return 1
            else:
                return 0
        else:
            arr.append(nums[i])
            return (getit(nums[:i]+nums[i+1:],count-1) + getit(nums[:i]+nums[i+1:],count))

def primeNum(num):
    for i in range(2,int(num/2)):
        if num%i == 0:
            return False
    return True

print(getit(nums,3))