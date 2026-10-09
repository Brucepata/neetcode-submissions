class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        min_price = prices[0]
 
        if len(prices) <= 1:
            return 0 

        l = 0
        r = 1

        while(r < len(prices)):
            if prices[r] < min_price:
                min_price = prices[r]
            profit = max(profit, prices[r]-min_price)
            
            r+=1
        
        return profit
            