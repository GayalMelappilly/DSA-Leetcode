class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = {'A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u'}
        left = right = ''
        l, r = 0, len(s)-1

        if l == r:
            return s

        while l <= r:
            if s[l] not in vowels:
                left += s[l]
                l += 1
                continue
            if s[r] not in vowels:
                right += s[r]
                r -= 1
                continue
            if l == r:
                return left + s[l] + right[::-1]
            left += s[r]
            right += s[l]
            l += 1
            r -= 1
            
        return left+right[::-1]

    

        