class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
    
        l1, l2 = len(word1), len(word2)
        longest_word = word1 if l1 > l2 else word2
        strg = ''  

        for i in range(len(longest_word)):
            if i < l1 and i < l2:
                strg += word1[i]+word2[i] 
            else:
                strg += longest_word[i:len(longest_word)]
                return strg

        return strg             