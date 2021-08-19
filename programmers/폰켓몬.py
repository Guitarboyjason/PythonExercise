

nums = [3,3,3,2,2,2]
arr= []
nums.sort()
n = 0
for i in range(len(nums)):
    if i == 0 or(nums[i] != nums[i-1]):
        arr.append(nums[i])
if len(arr) >= len(nums)/2:
    print(int(len(nums)/2))
else:
    print(len(arr))
print(arr)