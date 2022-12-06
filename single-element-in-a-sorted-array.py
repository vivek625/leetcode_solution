class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
#  1 solution     ----------------------------------------------------------------------------------------------------
        # for i in range(len(nums)):
            # if nums.count(nums[i]) < 2:
                # return nums[i]
# 2 solution --------------------------------------------------------------------------------------------------------------
        # return [nums[i] for i in range(len(nums)) if nums.count(nums[i]) < 2][0]
# 3  -------------------------------------------------------------------------------------------------------------
        s = 0
        for i in range(len(nums)):
            s ^= nums[i]
        return s
