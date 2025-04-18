class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        result = []
        #sorted
        for i in range(len(nums)-3):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1,len(nums)-2):
                if j > i + 1 and nums[j] == nums[j -1 ]:
                    continue
                
                left, right = j+1, len(nums) - 1
                
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[right] + nums[left]

                    if current_sum > target:
                        right -= 1
                    
                    elif current_sum < target:
                        left += 1
                    
                    else:
                        result.append([nums[i],nums[j],nums[left],nums[right]])
                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
        
        return result
