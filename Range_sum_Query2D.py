class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix_mat = []
        for i in matrix:
            x = []
            for j in i:
                if len(x)==0:
                    x.append(j)
                else:
                    x.append(x[-1]+j)
            self.prefix_mat.append(x)
                

    def sumRegion(self, x: int, y: int, p: int, q: int) -> int:
        ans = 0
        for i in range(x,p+1):
            if y-1<0:
                ans += self.prefix_mat[i][q]
            else:
                ans += self.prefix_mat[i][q]-self.prefix_mat[i][y-1]
        return ans
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
