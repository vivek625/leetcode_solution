class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        nums.sort()
        for i in nums:
            if i == target :
                return True
        return False
