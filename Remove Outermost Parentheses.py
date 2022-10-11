class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        k = []
        l = 0
        for i in s:
            if i == '(' and l > 0:
                k.append(i)
            elif i == ')' and l > 1:
                k.append(i)
            if i == '(' :
                   l += 1
            else:
                l -= 1
        return (''.join(k))
