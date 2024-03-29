class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        cur = float('-inf')
        res = 0
        for p in sorted(pairs,key = lambda  x:x[1]):
            if cur < p[0]: cur , res = p[1] ,res + 1
        return res
