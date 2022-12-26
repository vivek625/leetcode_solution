class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        # nums.sort()
        # s = []
        # for i in range(len(nums)):
        #     k = int(math.pow(nums[i],2))
        #     for j in range(len(nums)):
        #         if k == nums[j]:
        #             # print(nums[i],k)
        #             s.append(nums[i])
        #             s.append(k)
        # k = (len(set(s)))
        # if k > 1:
        #     return k
        # else:
        #     return -1
        nums = set(nums)
        s = set()
        ans = 1
        for n in nums:
            s.add(n)
            cur = 1
            while (n**2 in nums):
                s.add(n**2)
                n *= n
                cur += 1
            ans = max(ans,cur)
        return (ans if ans > 1 else -1)
