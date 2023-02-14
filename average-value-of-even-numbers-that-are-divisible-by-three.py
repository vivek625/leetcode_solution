class Solution:
    def averageValue(self, nums: List[int]) -> int:
        s = []
        for i in nums:
            if i % 2 == 0:
                if i % 3 == 0:
                    s.append(i)
        n = len(s)
        if len(s) == 0:
            return 0
        return sum(s)//n
