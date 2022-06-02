class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        x,y=len(matrix),len(matrix[0])
        ans = [[None] * x for _ in range(y)]
        for i in range(x):
            for j in range(y):
                ans[j][i]=matrix[i][j]
        
        return ans
