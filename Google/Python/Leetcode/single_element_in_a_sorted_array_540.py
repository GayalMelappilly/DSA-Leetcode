class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        leng = len(nums)-1
        l, r = 0, leng
        
        while l<r:
            mid = (l+r)//2

            if nums[mid] == nums[mid-1]:
                mid -= 1

            if nums[mid] != nums[mid+1]:
                return nums[mid]

            if mid == l:
                return nums[r]
            elif mid == 1:
                return nums[l]

            if mid%2 != 0:
                r = mid-1
            else:
                l = mid

        return nums[0]
                 
        