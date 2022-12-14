class Solution:
    def rob(self, nums: List[int]) -> int:
#       --------------------26 test case pass only------------------------------------
        # if len(nums) == 0:
        #     return 0
        # if len(nums) == 1:
        #     return nums[0]
        # n = len(nums)
        # s = []
        # i = 0
        # while  i < n:
        #     s.append(nums[i])
        #     i+= 2
        # return sum(s)
        
#     -----------------------------all test case pass ---------------------------------------
        s = [0,0]
        for i in range(len(nums)):
            if i % 2 == 0:
                s[0]= max(s[0]+nums[i],s[1])
            else:
                s[1] = max(s[1]+nums[i],s[0])
        return max(s)
