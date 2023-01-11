class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        # s = "leetcode"
        for i , j in (Counter(s).items()):
            if j == 1:
                return (s.index(i))
        return (-1)
