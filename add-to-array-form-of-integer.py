class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        s = int("".join(map(str,num)))
        sum_ = s+k
        k = ((str(sum_)))
        res = []
        for i in k:
            res.append(int(i))
        return (res)
