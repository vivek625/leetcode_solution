class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        s = [0]*len(nums)
        k = 0
        for i in range(len(nums)):
            start = i
            d = 1
            while not s[start]:
                s[start] = d
                start = nums[start]
                d +=1 
        return(len(set(s)))
