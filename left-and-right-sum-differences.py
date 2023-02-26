class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        # nums = [10,4,8,3]
        rev_nums= nums[::-1]
        right_sum = [0]
        left_sum = [0]
        ans = []
        k = 0
        l = 0
        for i in range(len(nums)-1):
            k += nums[i]
            right_sum.append(k)
            l += rev_nums[i]
            left_sum.append(l)
        left_sum = left_sum[::-1]
        # print(right_sum)
        # print(left_sum)
        for i in range(len(rev_nums)):
            ans.append(abs(right_sum[i]-left_sum[i]))
        return (ans)
