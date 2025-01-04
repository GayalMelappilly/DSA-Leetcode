class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:   

        leng = len(nums)
        arr_sum = nums[0]
        max_sum = 0

        for i in range(1,leng):
            if nums[i-1]<nums[i]:
                arr_sum += nums[i]
                if arr_sum>max_sum:
                    max_sum = arr_sum
            else:
                arr_sum = nums[i]
                
        if nums[0]>max_sum:
            return nums[0] 
        return max_sum        