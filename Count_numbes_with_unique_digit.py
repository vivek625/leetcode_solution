class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        ch = [9,9,8,7,6,5,4,3,2,1]
        res = 1
        pro = 1
        for i in range(n if n <= 10 else 10):
            pro *= ch[i]
            res += pro
        return res
