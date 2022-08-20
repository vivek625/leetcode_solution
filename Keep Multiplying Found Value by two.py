class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums.sort()
        s = original
        if original not in nums:
            return original
        else:
            k = []
            for i in range(0,len(nums)):
                if nums[i] != original:
                    k.append(nums[i])
                else:
                    original *= 2
        return (original)
