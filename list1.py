## Python function to search a target after sorting
def numbers(nums,target):
    if target not in nums:
        nums.append(target)
    sorted_list = sorted(nums)
    if target in sorted_list:
        return sorted_list.index(target)