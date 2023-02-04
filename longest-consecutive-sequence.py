class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        for i in nums:
            if i-1 not in nums:
                s = i
                while s in nums:
                    s += 1
                ans = max(ans,s-i)
        return ans
