class Solution:
    def baseNeg2(self, n: int) -> str:
        s = [1 << i for i in range(1,33,2)]
        for i in s:
            if n & i:
                n += i*2
        return (bin(n)[2:])
