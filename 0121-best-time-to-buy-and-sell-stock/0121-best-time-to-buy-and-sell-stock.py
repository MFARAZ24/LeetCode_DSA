class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_pr = prices[0]
        max_pr = 0
        for i in range(len(prices)):
            max_pr = prices[i]-min_pr
            if max_pr<=0:
                min_pr = prices[i]
            if max_pr>profit:
                profit = max_pr
        return profit

        