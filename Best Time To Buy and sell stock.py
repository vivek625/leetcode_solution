class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s = []
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                n = prices[i+1] - prices[i]
                s.append(n)
        return (sum(s))
