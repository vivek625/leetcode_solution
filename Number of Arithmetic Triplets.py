class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        s = 0
        for i in nums:
            k = i+diff
            a = k+diff
            if k in nums and a in nums:
                s += 1
        return (s)
