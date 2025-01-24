class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        k = n // 2

        mp = {}
        res = 0
        count = 0

        for num in nums:
            mp[num] = 1 + mp.get(num,0)

            if mp[num] > count:
                res = num
                count = mp[num]
        
        return res