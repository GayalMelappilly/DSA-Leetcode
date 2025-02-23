class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        leng = len(nums)
        i = 0
        low = 1

        while i <= leng-1:
            if nums[i] == i+1:
                i += 1
                continue
            if nums[i] <= leng and nums[i] > 0:
                j = nums[i]-1
                if nums[j] == nums[i]:
                    i += 1
                else:
                    nums[j], nums[i] = nums[i], nums[j]
                continue
            i += 1

        if nums[0] != low:
            return low
        
        for num in nums:
            if num != low:
                return low
            else:
                low += 1

        return leng + 1

        

                 



        