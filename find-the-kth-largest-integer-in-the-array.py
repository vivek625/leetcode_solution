class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        s =[]
        for i in range(len(nums)):
            s.append(int(nums[i]))
        s.sort(reverse=True)
        return str(s[k-1])
