class Solution:
    def numSquares(self , n):
        if int(math.sqrt(n))**2 == n:
            return 1
        for j in range(int(math.sqrt(n))+1):
            if int(math.sqrt(n-j*j))**2 == n - j * j:
                return 2
        while n % 4 == 0:
            n >>= 2
        if n % 8 == 7:
            return 4
        return 3
