def numbers(nums,target):
    if target not in nums:
        nums.append(target)
    sorted_list = sorted(nums)
    if target in sorted_list:
        return sorted_list.index(target)
print(numbers([0,3,2,6], target = 1))
        
