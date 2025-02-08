class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        l = 0
        max_len = 0
        count = 0
        vowels = {
            "a",
            "e",
            "i",
            "o",
            "u"
        }

        for i in range(len(s)):
            if i-l > k-1:
                if s[l] in vowels:
                    count -= 1
                l += 1
            if s[i] in vowels:
                count += 1
            if count > max_len:
                max_len = count 
        return max_len   



            

            

        