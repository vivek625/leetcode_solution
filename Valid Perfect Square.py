class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        start = 0
        end = num/2
        while start <= end:
            mid = (start + end)//2
            if mid * mid == num:
                return(True)
            elif mid * mid > num:
                end = mid - 1
            elif mid * mid < num:
                start = mid + 1
        return (False)
