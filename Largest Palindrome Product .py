class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        min_ = 10**(n-1)
        max_ = 10**n-1
        pal = 0
        for i in range(max_, min_ - 1, -2): 
            if i * i < pal:
                break
            for j in range(max_, i - 1, -2):
                prod = i*j
                if prod % 11 != 0 and prod >= pal:
                    continue
                if str(prod) == str(prod)[::-1]:
                    pal = prod
        return (pal % 1337)
