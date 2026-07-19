class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        trade_period = len(prices)
        profit = 0

        while r<trade_period:
            if(prices[l]>=prices[r]):
                l=r
                r+=1
            else:
                curr_profit = prices[r]-prices[l]
                profit = max(profit,curr_profit)
                r+=1
        return profit
