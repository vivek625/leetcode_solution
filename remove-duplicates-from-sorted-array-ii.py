class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        set_nums = list(set(nums))
        cont = {i:nums.count(i) for i in set_nums}
        for i in set_nums:
            if cont[i] > 2:
                for j in range(cont[i]-2):
                    nums.remove(i)
        return len(nums)
