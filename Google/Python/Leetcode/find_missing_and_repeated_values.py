class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        ans = [None, None]
        n = len(grid)
        pos = [False] * (n*n)
        total = ((n*n)*((n*n)+1))//2

        for mat in grid:
            for num in mat:
                if pos[num-1] == True:
                    ans[0] = num
                else:
                    pos[num-1] = True
                    total -= num
                    
        ans[1] = total 
        return ans
        
        