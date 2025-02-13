def twoNumberSum(array,target):
    array.sort()

    left, right = 0, len(array) - 1

    while left < right:
        sum = array[left] + array[right]

        if sum == target:
            return [array[left],array[right]]
        
        elif sum < target:
            left += 1

        elif sum > target:
            right -= 1

    return []