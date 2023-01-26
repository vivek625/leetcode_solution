class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        k = str(num)
        l = int(k[::-1])
        m = str(l)
        mm = int(m[::-1])
        if num == mm:
            return True
        else:
            return False
