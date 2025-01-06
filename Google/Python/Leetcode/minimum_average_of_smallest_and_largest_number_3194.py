class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        left = 0
        right = len(nums) - 1
        min_avg = float('inf')
        nums.sort()

        while left <= right:
            sum = nums[left] + nums[right]
            avg = sum / 2
            min_avg = min(avg,min_avg)
            left += 1
            right -=1

        return min_avg