class Solution:
    def maximumGap(self, nums: List[int]) -> int:

        if len(nums)<2:
            return 0

        nums = sorted(set(nums))
        maxGap = 0

        for i in range(len(nums)):
            if i < len(nums)-1:
                if nums[i+1] - nums[i] > maxGap:
                    maxGap = nums[i+1] - nums[i]

        return maxGap    

        