class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        r = 0
        l = n
        temp = 0
        new_arr = []

        for i in range(n):
            new_arr.append(nums[r])
            new_arr.append(nums[l])
            r += 1
            l += 1        

        return new_arr   
        