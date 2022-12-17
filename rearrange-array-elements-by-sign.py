class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        k=[]
        l =[]
        for i in nums:
            if i > 0:
                k.append(i)
            else:
                l.append(i)
        n =[]
        for i in range(len(k)):
            n.append(k[i])
            n.append(l[i])
        return (n)
