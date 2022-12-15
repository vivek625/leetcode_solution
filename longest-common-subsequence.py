class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # n = len(text1)
        # s = 0
        # k= []
        # for i in range(n-1):
        #     for j in range(i,len(text2)):
        #         if text1[i] == text2[j]:
        #             k.append(text1[i])
        #             k.append(text2[j])
        #             s +=1
        # return (s)
        memo = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1) ]
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    memo[i+1][j+1] = memo[i][j] + 1
                else:
                    memo[i+1][j+1] = max(memo[i+1][j], memo[i][j+1])
        return (max((max(row) for row in memo)))
