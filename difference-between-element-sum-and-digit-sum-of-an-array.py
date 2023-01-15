class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        # nums = [1,15,6,3]
        su = sum(nums)
        s = []
        k = "".join(map(str,nums))
        for i in range(len(k)):
            s.append(int(k[i]))
        return (abs(su-sum(s)))
