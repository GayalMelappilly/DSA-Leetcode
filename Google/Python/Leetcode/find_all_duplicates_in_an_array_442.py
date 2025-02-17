class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        check = [1] * len(nums)
        res = []

        for num in nums:
            idx = num-1
            if check[idx] == 0:
                res.append(num)
            else:
                check[num-1] = 0
        return res

