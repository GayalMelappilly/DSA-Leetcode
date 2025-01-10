class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

# [ 2 , 3 , 1 , 2 , 4 , 3 ]   
#   l   r   r   r   r   r
#   r   l   l   l   l   l

#   s = 2 
#   s = 2 + 3 = 5
#   s = 2 + 3 + 1 = 6
#   s = 3 + 1 + 2 = 6
#   s = 1 + 2 + 4 = 7
#   s = 2 + 4 + 3 = 9
#   s = 4 + 3 = 7
#   s = 3

# returns 2

        leng = len(nums)
        subarray_sum = 0

        if sum(nums)==target:
            return leng

        l, r = 0, 0
        subarray_sum = nums[l]
        subarray_len = leng+2

        while l<=r:
            if subarray_sum >= target:
                if r-l < subarray_len:
                    subarray_len = (r-l)+1
                subarray_sum -= nums[l]
                l += 1
            elif subarray_sum < target:
                if r<leng-1:
                    r += 1
                    subarray_sum += nums[r]
                else:
                    l += 1

        if subarray_len>leng:
            return 0            
        return subarray_len       
