class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        best_price = prices[0]
        for i in range(1,len(prices)):
            if prices[i]>best_price:
                max_profit = max(max_profit,prices[i]-best_price)
            best_price = min(best_price,prices[i])
        return max_profit
