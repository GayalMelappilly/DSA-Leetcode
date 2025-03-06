class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        l = 0
        count = 1
        for r in range(1,len(nums)):
            if nums[l] == nums[r]:
                if count < 2:
                    count += 1
                    l+=1
                    nums[l] = nums[r]
            else:
                l +=1
                nums[l] = nums[r]
                count = 1
        return l+1

        # leng = len(nums)
        # count = 0
        # prev = -1
        # i = leng
        # idx = 0

        # while idx < leng:
        #     if prev >= 0 and nums[idx] == nums[prev]:
        #         count += 1
        #         if idx == leng - 1 and count >= 2:
        #             for j in range(count-1):
        #                 nums.pop()
        #             break
        #     else:
        #         if count >= 2:
        #             i = (idx-count)+1
        #             count = idx-i
        #             while i+count<leng:
        #                 nums[i] = nums[i+count]
        #                 i += 1
        #             for j in range(count):
        #                 nums.pop()   
        #         leng = len(nums)
        #         idx -= count
        #         count = 0
        #     prev = idx
        #     idx += 1
        # return len(nums)


            
        