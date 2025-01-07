class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        prev_num = nums[0]
        flag = nums[0] > nums[len(nums)-1]

        if flag is True:
            for num in nums:
                if prev_num < num:
                    return False
                prev_num = num    
        else:
            for num in nums:
                if prev_num > num:
                    return False
                prev_num = num          

        return True             