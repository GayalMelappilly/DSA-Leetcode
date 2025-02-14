class Solution:
    def longestMountain(self, arr: List[int]) -> int:

        peak = 0
        leng = 0
        max_leng = 0
        start = -1

        for i in range(len(arr)):

            if i == len(arr)-1:
                if peak == 2:
                    leng = (i-start)+1
                    if leng > max_leng:
                        max_leng = leng
                return max_leng   

            l = arr[i]
            r = arr[i + 1]

            if l == r:
                if peak == 2:
                    leng = (i-start)+1
                    if leng > max_leng:
                        max_leng = leng
                start = -1
                peak = 0
                continue
            if peak == 0 and l<r:
                start = i
                peak = 1
                continue
            elif peak == 1 and l>r:
                peak = 2
                continue
            elif peak == 2 and l<r and start > -1:
                leng = (i-start)+1
                if leng > max_leng:
                    max_leng = leng
                leng = 0
                start = i
                peak = 1





        