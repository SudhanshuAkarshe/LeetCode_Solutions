class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        high = 0
        buy = prices[0]
        for i in range(1,len(prices)):
            
            if prices[i]<buy:
                buy = prices[i]
            elif (prices[i]-buy)>high:
                high = prices[i]-buy
        return high            
        