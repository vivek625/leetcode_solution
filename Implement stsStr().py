class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l,r = 0,len(needle)
        for i in range(len(haystack)):
            if (haystack[l:r]) == needle:
                return (l)
            l+=1
            r+=1
        return (-1)
