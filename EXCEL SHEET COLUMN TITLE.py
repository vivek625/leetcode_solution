class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = "" # consider an empty string
        while columnNumber>0: 
            columnNumber-=1
            s = chr(columnNumber%26 + 65) + s  #considering the ascii values of the alphabets 
            columnNumber//=26
        return(s)
