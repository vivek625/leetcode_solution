class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        # nums = [4,2,5,7]
        odd = []
        even = []
        result = []
        for i in nums:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        print(even)
        print(odd)
        for i in range(len(even)):
            result.append(even[i])
            result.append(odd[i])
        return (result)
