class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        leng = len(prices)

        for i in range(leng):
            if i>=leng-1:
                return profit
            if prices[i]<prices[i+1]:
                profit += prices[i+1]-prices[i]   