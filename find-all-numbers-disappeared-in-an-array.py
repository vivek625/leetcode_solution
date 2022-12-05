class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
#         n = len(nums)+1
#         s = []
#         for i in range(1,n):
#             if i not in nums:
#                 s.append(i)
#         return (s)
        n = [ i for i in range(1,len(nums)+1)]
        k = list(set(n)-set(nums))
        return k
