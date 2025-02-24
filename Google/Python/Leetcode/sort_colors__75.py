class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        leng = len(nums)

        if leng == 1:
            return nums

        freq = [0]*3
        sorted_colors = [0]*leng

        for num in nums:
            freq[num]+=1

        freq[0] -= 1
        freq[1] += freq[0]
        freq[2] += freq[1]

        i = 0
        pos = 0

        while i < leng:
            if i>freq[pos]:
                pos += 1
                if i>freq[pos]:
                    pos += 1
            nums[i] = pos
            i += 1