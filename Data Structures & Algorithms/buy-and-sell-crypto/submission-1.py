class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = float("-inf")
        l,r = 0, 0 

        for r in range(len(prices)):
            profit = prices[r] - prices[l]

            if profit > max_profit:
                l = r
                max_profit = profit
        
        return profit
            