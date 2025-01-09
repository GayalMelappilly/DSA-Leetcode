class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        right = 1
        length = 0

        while right < len(nums):
            difference = nums[right] - nums[left]

            if difference == 1:
                length = max(length, right-left+1)
                
            if difference <= 1:
                right += 1
            else:
                left += 1
        
        return length 