class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        s= 1
        diff = k
        res = list(range(1,n-k+1))
        for i in range(k):
            res.append(res[-1]+s*diff)
            s *= -1
            diff -= 1
        return (res)
