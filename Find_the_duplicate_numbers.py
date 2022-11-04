from typing import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = Counter(nums)
        for i in s:
            if s[i] >= 2:
                return i
