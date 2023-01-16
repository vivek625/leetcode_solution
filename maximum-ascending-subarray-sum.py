class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        s = 0
        r = 0
        for i in range(len(nums)):
            if nums[i-1] < nums[i]:
                s += nums[i]
            else:
                s = nums[i]
            r = max(r,s)
        return r
