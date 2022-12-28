class Solution:
    def countSubstrings(self, s: str) -> int:
        k = 0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                tem = s[i:j]
                if tem == tem[::-1]:
                    k+=1
        return k
