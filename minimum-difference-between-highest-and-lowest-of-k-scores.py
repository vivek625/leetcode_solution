class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) <= 1:
            return 0
        s =[]
        nums.sort()
        for i in range(len(nums)-k+1):
            m = (nums[i+k-1]-nums[i])
            s.append(m)
        return min(s)
                
