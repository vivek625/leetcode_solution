class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        sum_num = sum(nums)
        left_Sum = 0
        s = [math.inf,math.inf]
        for i , j in enumerate(nums):
            left_Sum  += j
            left_avg = left_Sum//(i+1)
            right_avg = (sum_num - left_Sum) // (n-i-1) if (n-i-1) != 0 else 0
            avg = abs(left_avg - right_avg)
            s = min(s,[avg,i])
        return(s[1])
