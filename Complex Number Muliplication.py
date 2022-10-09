class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a = num1.index("+")
        b = num2.index("+")
        x1 = int(num1[:a])
        y1 = int(num1[a+1:-1])
        x2 = int(num2[:b])
        y2 = int(num2[b+1:-1])
        ss = str(x1*x2 - y1*y2)
        ss1 = str(x1*y2 + x2*y1)
        return (ss+"+"+ss1+"i")
