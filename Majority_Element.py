class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        v = 1
        k = nums[0] 
        n = len(nums)
        for i in range(1,n):
            if v == 0:
                k = nums[i]
                v = 1
            else:
                if nums[i] == k:
                    v += 1
                else:
                    v -= 1
        return k
