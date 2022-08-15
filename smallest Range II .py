class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = nums[-1]-nums[0]
        for i in range(1,len(nums)):
            l = nums[:i]
            r = nums[i:]
        #     print(l)
        #     print(r)
            mini = min(l[0]+k,r[0]-k)
            maxi = max(l[-1]+k, r[-1]-k)
            ans = min(ans, maxi-mini)
        return (ans)
