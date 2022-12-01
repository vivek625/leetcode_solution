class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)//2
        s1 = s[:n]
        s2 = s[n:]
        v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        re = []
        res = []
        for i in s1:
            for j in v:
                if i == j:
                    re.append(i)
        for i in s2:
            for j in v:
                if i == j:
                    res.append(i)
        if len(re) == len(res):
            return (True)
        else:
            return (False)
