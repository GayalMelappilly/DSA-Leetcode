class Solution:
    def getSum(self, a: int, b: int) -> int:

        return ((a^b)+((a&b)<<1))

        
        