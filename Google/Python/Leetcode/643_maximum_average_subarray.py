class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        current_sum = maxSum = sum(nums[:k])

        for i in range(k,len(nums)):

            current_sum += nums[i] - nums[i - k]

            maxSum = max(maxSum, current_sum)

        return maxSum / k
