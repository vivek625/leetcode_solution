class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        s = len(nums)
        even = nums[0:s:2]
        even.sort()
        odd = nums[1:s:2]
        odd.sort(reverse=True)
        return ([even[i//2] if i % 2 == 0 else odd[i//2] for i in range(s)])
