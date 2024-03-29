class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a,b = 0,int(math.sqrt(c))
        while (a<=b):
            if a*a + b*b == c:
                return True
            elif a*a + b*b < c:
                a += 1
            else:
                b -= 1
        return False
