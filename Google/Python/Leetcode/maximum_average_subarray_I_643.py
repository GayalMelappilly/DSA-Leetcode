class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
  
        l = 0
        subarray_sum = 0
        
        for r in range(len(nums)):
            if r-l == k:
                subarray_sum -= nums[l]
                subarray_sum += nums[r]
                if subarray_sum/k > max_avg:
                    max_avg = subarray_sum/k
                l += 1
            else:    
                subarray_sum += nums[r]
                if r-l == k-1:
                    max_avg = subarray_sum/k  

        return max_avg