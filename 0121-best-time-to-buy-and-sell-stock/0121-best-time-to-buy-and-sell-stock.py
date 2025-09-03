class Solution:
    def maxProfit(self, prices) -> int:
        left, res = 0, 0
        for right in range(len(prices)):
            if prices[right] < prices[left]:
                left = right

            res = max(res, prices[right] - prices[left])
        return res
