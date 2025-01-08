class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        lastIdx = len(nums)-1

        for i in range(len(nums)-2, -1, -1):
            if i+nums[i] >= lastIdx:
                lastIdx = i

        return lastIdx == 0        