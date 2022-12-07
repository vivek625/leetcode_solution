class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_ = min(nums)
        s = 0
        for i in nums:
            s = s +  i - min_
        return (s)
