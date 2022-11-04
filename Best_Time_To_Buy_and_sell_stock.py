class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_ = 0
        l = 0
        r = 1
        while (r<len(prices)):
            max_ = max(max_,prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
                r += 1
            else:
                r += 1
        return max_
