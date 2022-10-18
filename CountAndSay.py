class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        x = self.countAndSay(n-1)
        s = ""
        y = x[0]
        t = 1
        for i in range(1,len(x)):
            if x[i] == y:
                t += 1
            else:
                s += str(t)
                s += str(y)
                y = x[i]
                t = 1
        s += str(t)
        s += str(y)
        return s
