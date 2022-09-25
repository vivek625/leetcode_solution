class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        s = []
        for i in range(1,n+1):
            s.append(i)
        com = combinations(s,k)  # combinations module in python   --> from itertools import combinations
        return com
