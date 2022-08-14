class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        d = Counter(nums)
        pair = npair = 0
        for i in d.keys():
        #     print(i)
            if d[i] >= 2:
                pair += d[i]//2
        #         print(pair)
            npair += d[i]%2
        #     print(npair)
        return ([pair,npair])
