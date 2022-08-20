class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        k = max(nums)
        for i in nums:
            if i != k:
                if i*2 > k:
                    return -1
        return nums.index(k)
