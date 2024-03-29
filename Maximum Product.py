class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxval = minval = ans = nums[0]
        n = len(nums)
        for i in range(1,n):
            temp_min = minval
            temp_max = maxval
            maxval = max(temp_min * nums[i],temp_max * nums[i],nums[i])
            minval = min(temp_min * nums[i],temp_max * nums[i],nums[i])
            ans = max(ans,maxval)
        return ans
