class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        s=int(math.sqrt(num))
        ss  = 1
        for i in range(2,s+1):
            if num % i == 0:
                t = num // i
                ss += t+i
        if (ss) == num:
            return (True)
        else:
            return (False)
    
