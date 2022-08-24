def zero(n):
    if '0' in str(n):
        return 1
    return 0

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        i = 1
        j = n-1
        while (zero(i) or zero(j)):
            i+=1
            j-=1
        return [i,j]
