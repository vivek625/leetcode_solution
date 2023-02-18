class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        s = []
        for i in nums:
            s.append(i)
            k = str(i)
            l = int(k[::-1])
            s.append(l)
        return len(set(s))
