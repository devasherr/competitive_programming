class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy, sell = prices[0], prices[0]

        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
                sell = prices[i]
            else:
                sell = max(sell, prices[i])
                res = max(res, sell - buy)
        return res