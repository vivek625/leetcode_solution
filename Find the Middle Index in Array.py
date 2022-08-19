class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        s = 0
        t = sum(nums)
        for i, j in enumerate(nums):
            t  -= j
            if s == t:
                return i
            s += j
        return -1
