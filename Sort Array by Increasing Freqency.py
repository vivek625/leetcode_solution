class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # nums = [1,1,2,2,2,3]
        di = Counter(nums)

        arr = sorted(di.items(),key = lambda x : (x[1],-x[0]))

        res = []
        for key,val in arr:
            res+=[key]*val
        return res
