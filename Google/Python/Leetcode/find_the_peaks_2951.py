class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:

        peaks = []

        for index, num in enumerate(mountain):
            if index != 0 and index != len(mountain)-1:
                if num>mountain[index+1] and num>mountain[index-1]:
                    peaks.append(index)

        return peaks       