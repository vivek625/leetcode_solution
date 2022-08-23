class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        partial_sum = max_sum = nums[0]
        for i in range(1,len(nums)):
            partial_sum = max(nums[i],(partial_sum + nums[i]))
            max_sum = max(max_sum , partial_sum)
        return max_sum
