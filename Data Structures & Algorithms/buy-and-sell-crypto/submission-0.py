class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #buy low and sell high
        #l is buying
        #r is slling
        # profit when pirces[r] > prices[l]
        #reset l when our right is less than l, 

        max_profit = 0

        if len(prices) < 1:
            return max_profit

        l = 0 
        r = 1

        while(r < len(prices)):
            cur_profit = prices[r] - prices[l]

            if cur_profit < 0:
                l = r
            else:
                max_profit = max(max_profit, cur_profit)
                r += 1

            #reset r pointer. 
        

        return max_profit



        