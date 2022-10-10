class Solution:
    def decodeString(self, s: str) -> str:
        p = ""
        n = 0
        stack = []
        for i in s:
            if i.isdigit():
                n = n * 10 + int(i)
            elif i == '[':
                stack.append((p,n))
                p = ''
                n = 0
            elif i == ']':
                prev_p , prev_n = stack.pop()
                p = prev_p + prev_n*p
            else:
                p += i
        return(p)        
