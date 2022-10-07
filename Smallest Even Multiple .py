class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        s = n*2
        x = 0
        for i in range(2,s+1):
            if (i% 2 == 0) and (i % n == 0):
                x = i
                break
        return x
