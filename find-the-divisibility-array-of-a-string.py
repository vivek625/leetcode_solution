class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        ans = []
        k = 0
        for i in word:
            k = k*10+int(i)
            if k%m == 0:
                ans.append(1)
            else:
                ans.append(0)
            k = k%m
        return ans
