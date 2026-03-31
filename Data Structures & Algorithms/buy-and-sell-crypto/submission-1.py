class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_amount = prices[0]
        ans = 0
        for i in range(1, len(prices)):
            ans = max(ans, prices[i] - min_amount)
            min_amount = min(min_amount, prices[i])

        return ans;