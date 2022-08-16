class Solution:
    def replaceDigits(self, s: str) -> str:
        st = ''
        t = 0
        for i in range(0,len(s),2):
            st+=s[i]
            t = ord(s[i])
            if i != len(s)-1:
                st += chr(t+int(s[i+1]))
        return (st)
