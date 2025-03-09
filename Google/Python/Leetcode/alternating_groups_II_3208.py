class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:

        doubled_array = colors
        j = 0

        for color in colors:
            if j == k-1:
                break
            j += 1
            doubled_array.append(color)
        
        left = 0
        count = 0

        for idx, right in enumerate(doubled_array):

            if idx > 0 and right == doubled_array[idx-1]:
                left = idx
            
            if idx - left + 1 >= k:
                count += 1
        
        return count
            