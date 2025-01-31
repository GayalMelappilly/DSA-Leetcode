class Solution:
    def findMin(self, nums: List[int]) -> int:

        leng = len(nums)

        for i in range(leng):
            if i == leng-1:
                return nums[0]
            if nums[i]>nums[i+1]:
                return nums[i+1]
