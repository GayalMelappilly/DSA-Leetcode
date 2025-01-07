class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        leng = len(candies)
        top = max(candies)

        for i in range(leng):
            if candies[i]+extraCandies>=top:
                candies[i] = True
            else:
                candies[i] = False
                
        return candies     
        
        