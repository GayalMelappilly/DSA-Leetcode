class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        highest_alt = 0
        pf = 0

        for i in range(len(gain)):
            pf = pf + gain[i]
            if pf>highest_alt:
                highest_alt = pf
        return highest_alt
            



        