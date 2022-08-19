class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rsum = sum(nums)
        lsum = 0
        for i , j in enumerate(nums):
            rsum -= j
            if lsum == rsum :
                return i
            lsum += j
        return -1
