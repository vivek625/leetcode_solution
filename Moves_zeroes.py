class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        if len(nums) == 1:
            return nums
        s = []
        k = []
        for i in nums:
            if i == 0:
                k.append(i)
            else:
                s.append(i)
        for j in k:
            s.append(j)
        return s
        """
        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zero],nums[i] = nums[i] , nums[zero]
                zero += 1
