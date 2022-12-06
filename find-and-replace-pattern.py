class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        pattern_d ={}
        for i , val in enumerate(pattern):
            pattern_d[val] = pattern_d.get(val,[]) + [i]
        for w in words:
            d ={}
            for i , val in enumerate(w):
                d[val] = d.get(val,[])+[i]
            if (sorted(d.values()) == sorted(pattern_d.values())):
                res.append(w)
        return res
