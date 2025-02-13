def twoNumberSum(array,target):
    nums = {}

    for num in array:
        if target - num in nums:
            return [target-num, num]
        
        else:
            nums[num] = True

    return []