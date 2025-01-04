class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bought = prices[0]
        profit = 0

        for i in prices[1:]:
            if bought > i:
                bought = i
            
            profit = max(profit, i - bought)
            
        return profit