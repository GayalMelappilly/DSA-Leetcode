class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        leng = len(nums)

        return leng*(leng+1)//2-sum(nums)        

        