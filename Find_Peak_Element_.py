class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        s = max(nums)
        for i in range(len(nums)):
            if nums[i] == s:
                return i
