class Solution:
    def trailingZeroes(self, n: int) -> int:
        # z = []
        # s = factorial(n)
        # k = str(s)
        # for i in k:
        #     if i == '0':
        #       z.append(i)
        # return (len(z))
        x   = 5
        res = 0
        while x <= n:
            res += n//x
            x  *= 5
        return  (res)
