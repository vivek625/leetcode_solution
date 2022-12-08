class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        start, end, n = 1, 1, len(nums)
        out = [1]*n 
        for i in range(len(nums)):
            out[i] *= start
            start *= nums[i]
            out[n-i-1] *= end
            end *= nums[n-i-1]
        return (out)
