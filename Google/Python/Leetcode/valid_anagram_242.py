class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        prev_map = {}

        if len(s) != len(t):
            return False

        for char in s:
            if char in prev_map:
                prev_map[char] += 1
            else:    
                prev_map[char] = 1
        

        for char in t:
            if char in prev_map:
                if prev_map[char] == 0:
                    return False
                else:    
                    prev_map[char] -= 1
            else:
                return False
        return True                 
            
        