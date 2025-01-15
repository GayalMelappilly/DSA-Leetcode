class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        prev_map = {}

        for char in s:
            if char in prev_map:
                prev_map[char] += 1
            else:
                prev_map[char] = 1


        for char in t:
            if char in prev_map:
                prev_map[char] -= 1
                if prev_map[char] < 0:
                    return char
            else:
                return char                
        