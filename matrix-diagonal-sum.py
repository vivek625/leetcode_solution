class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        mata = mat[::-1]
        s = []
        k = []
        for i in range(len(mat)):
            s.append(mat[i][i])
            s.append(mata[i][i])
        if len(mat) % 2 == 1:
            mid = len(mat)//2
            k.append(mat[mid][mid])
        return(sum(s)-sum(k))
