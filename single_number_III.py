class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        s = set()
        for i in nums:
            if i not in s:
                s.add(i)
            else:
                s.remove(i)
        return list(s)
