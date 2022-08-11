class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count=0
        ans=0
        for i in range(len(nums)-1):
            j=i+1
            if nums[i]>=nums[j]:
                count+=nums[i]-nums[j]+1
                nums[j]+=count
                ans+=count
                count=0
        return (ans)
