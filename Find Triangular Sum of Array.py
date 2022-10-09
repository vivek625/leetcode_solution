class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        m = len(nums) - 1
        mCk = 1
        result = 0
        for k, num in enumerate(nums):
            result = (result + mCk * num) % 10
            # print("r",result)
            mCk *= m - k
            # print("mc",mCk)
            mCk //= k + 1
            # print("mc",mCk)
        return (result)
