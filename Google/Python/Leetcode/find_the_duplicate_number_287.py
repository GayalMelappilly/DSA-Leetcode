class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        k = [0]*len(nums)

        for i in nums:
            k[i] += 1
            if k[i] > 1:
                return i
        