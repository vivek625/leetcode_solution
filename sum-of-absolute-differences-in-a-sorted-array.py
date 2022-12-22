class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
#       ----------------------26 test case pass only --------------------------------------------------------------------------------
        # s = []
        # for i in range(len(nums)):
        #     n =[]
        #     for j in range(len(nums)):
        #         if j != i:
        #             sum_ = abs(nums[i]-nums[j])
        #             n.append(sum_)
        #     s.append(sum(n))
        # return(s)
        # -----------------------O(n) time complexity----------------------------------
        n = len(nums)
        s = 0
        sum_ = sum(nums)
        res = []
        for i , num in enumerate(nums):
        #     print(num)
            sum_ -= num
            k = sum_ - (n-1-i) * num + i*num-s
            
            res.append(k)
            s += num
        return (res)
