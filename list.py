def number(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if (nums[i] == nums[j]):
                continue
            elif (nums[i] + nums[j] == target):
                return (i,j)
print(number([2,7,11,15], target = 9))