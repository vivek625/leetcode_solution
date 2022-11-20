class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        s = 0 
        for i in range(len(nums)-1):
            s = max(s,abs(nums[i]-nums[i+1]))
        return s
