class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        i = len(nums) - 1
        j = len(nums) - 2    
        while j > -1:
            if j + nums[j] >= i:
                i = j
                j -= 1
                
            else:
                j -= 1
        if i <= 0:
            return True
        else:
            return False
