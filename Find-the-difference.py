class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cot = Counter(t)
        cos = Counter(s)
        res = cot - cos
        for i , j in res.items():
            if j == 1:
                return i
