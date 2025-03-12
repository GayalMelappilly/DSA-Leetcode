class Solution:
    def maximumCount(self, nums: List[int]) -> int:

        leng = len(nums)

        mid = leng//2
        count = 0

        if nums[0] > 0:
            return leng
        if nums[leng-1] < 0:
            return leng

        if nums[0] == 0 and nums[leng-1] == 0:
            return 0
        
        if nums[mid] > 0:
            while True:
                mid -= 1
                if nums[mid] <= 0:
                    return (leng-mid)-1

        if nums[mid] < 0:
            while True:
                mid += 1
                if nums[mid] >= 0:
                    return mid
        
        if nums[mid] == 0:
            if nums[mid-1] < 0 and nums[mid+1] > 0:
                return mid
            while True:
                count += 1
                if nums[mid-count] != 0 and nums[mid+count] == 0:
                    return (mid-count)+1
                if nums[mid-count] == 0 and nums[mid+count] != 0:
                    return leng - (mid+count-1)
                    



        









        