class Solution:
    def pivotInteger(self, n: int) -> int:
        # pivot intger
        # import math
        # n = 4
        s = [ i for i in range(n+1)]
        p= int(math.sqrt(sum(s)))
        l = [i for i in range(1,p+1)]
        ll = [i for i in range(p,n+1)]
        if sum(l) == sum(ll):
            return (p)
        return (-1)
