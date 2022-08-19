class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        s = 0
        for i in range(0,len(colors)):
            if colors[i] != colors[0]:
                s = max(s,i)
            if colors[i] != colors[-1]:
                s = max(s,len(colors)-i-1)
        return s
