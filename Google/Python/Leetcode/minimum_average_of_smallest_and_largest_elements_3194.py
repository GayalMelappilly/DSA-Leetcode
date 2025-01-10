class Solution:
    def minimumAverage(self, nums: List[int]) -> float:

        n = len(nums)
        l = n - 1
        min_element, max_element = 0, 0
        nums.sort()

        averages = nums[l]

        for r in range(n//2):
            min_element = nums[r]
            max_element = nums[l]

            if (max_element+min_element)/2 < averages:
                averages = (max_element+min_element)/2
            
            l -= 1

        return averages    
        