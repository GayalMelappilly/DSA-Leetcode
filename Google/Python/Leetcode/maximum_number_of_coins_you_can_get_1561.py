class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        piles.sort()

        coins = 0
        leng = len(piles)
        my_choice = leng
        i = 0

        while i*3 != leng:

            my_choice -= 2
            i += 1
            coins += piles[my_choice]

        return coins    
        
        