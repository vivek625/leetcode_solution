class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        k = sorted(Counter(word1).values())
        k1 = sorted(Counter(word2).values())
        s1 = set(word1)
        s2 = set(word2)
        return (k == k1 and s1 == s2)
