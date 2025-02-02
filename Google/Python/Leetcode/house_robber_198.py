class Solution:
    def rob(self, nums: List[int]) -> int:

        leng = len(nums)

        if leng == 1:
            return nums[0]

        max_money = [0] * leng
        max_money[0] = nums[0]

        max_money[1] = max(nums[0], nums[1])

        if leng == 2:
            return max_money[1]

        for i in range(2, leng):
            if nums[i]+max_money[i-2]>max_money[i-1]:
                max_money[i] = nums[i]+max_money[i-2]
            else:
                max_money[i] = max_money[i-1]
        
        if max_money[leng-1] == 0:
            return max_money[leng-2]
        else:
            return max_money[leng-1]       







        

        




        



              

        