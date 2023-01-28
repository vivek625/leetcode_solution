class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        # '''ans = 0
        # com = combinations(nums,2)
        # for i in com:
        #     for j in range(31,-1,-1):
        #         b1 = i[0] >> j & 1
        #         b2 = i[1] >> j & 1
        #         ans += not(b1 == b2)
        # '''
        ans = 0
        
        for i in range(32):
            a , b = 0,0
            m = 1 << i
            for num in nums:
                if m & num:
                    a += 1
                else:
                    b += 1
            ans += a * b
        return ans
                
