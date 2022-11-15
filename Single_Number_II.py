class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sum_ = sum(set(nums))
        sum_nums = sum(nums)
        res = ((3*sum_)-sum_nums)//2
        return res
