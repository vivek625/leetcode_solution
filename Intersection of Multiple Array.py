class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        all_nums = []
        ans =[]
        l = len(nums)
        for i in nums:
            all_nums += i
        from collection import Counter
        d = Counter(all_nums)
        for j in d.keys():
            if d[j] == l:
                ans.append(j)
        return sorted(ans)
