class Solution:
    def removeDuplicates(self, s: str) -> str:
        k = []
        for i in s:
            if k and i == k[-1]:
                k.pop()
            else:
                k.append(i)
        return ''.join(k)
