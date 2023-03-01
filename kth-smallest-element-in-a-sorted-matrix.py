class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        k  = k-1
        s = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                s.append(matrix[i][j])
        s.sort()
        for i in range(len(s)):
            if i == k:
                return s[i]
