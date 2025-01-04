class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        leng = len(nums)

        for index,num in enumerate(nums):
            if index != 0 and index != leng-1:
                if num>nums[index-1] and num>nums[index+1]:
                    return index
        
        if nums[0]>nums[leng-1]:
            return 0
        else:
            return leng-1    