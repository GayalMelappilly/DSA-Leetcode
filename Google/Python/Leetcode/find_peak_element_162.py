class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        leng = len(nums)

        if leng == 1:
            return 0
        
        if leng == 2:
            if nums[0]<nums[1]:
                return 1
            return 0

        l, r = 0, leng-1

        if nums[l]>nums[l+1]:
            return l
        if nums[r]>nums[r-1]:
            return r

        while l<r:
            mid = (l+r)//2
            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            if nums[mid]<nums[mid+1]:
                l = mid
            elif nums[mid]<nums[mid-1]:
                r = mid 
