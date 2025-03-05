class Solution:
    def coloredCells(self, n: int) -> int:

        if n==1:
            return n

        eq = 2*(n-1)
        
        return ((eq+1)*(eq+1)) - (n*eq)
        