class Solution:
    def generate(self,numRows : int) -> List[List[int]]:
        '''for i in range(n):
            for j in range(n-i+1):
                print(end = " ")
            for j in range(i+1):
                return (factorial(i)//(factorial(j)*factorial(i-j)))
            print()'''
        '''upper is the same of example format of pascal's triangle
        '''
        # numRows = 5
        s = [[1]]
        for i in range(numRows-1):
            temp = [1]
            for j in range(1, i+1):
                temp.append(s[i][j-1] + s[i][j])
            temp.append(1)
            s.append(temp)
        return (s)
