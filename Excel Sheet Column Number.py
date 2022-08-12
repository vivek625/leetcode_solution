class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # columnTitle = "A"
        columnTitle = columnTitle[::-1]
        sum = 0
        for i in range(len(columnTitle)):
        #     print(ord(columnTitle[i]))
            sum += (ord(columnTitle[i])-64)*(26**i)
        #     print(sum)
        return (sum)
