class Solution:
    def reverseWords(self, s: str) -> str:
        k = (" ".join(s.split()[::-1]))
        return k
