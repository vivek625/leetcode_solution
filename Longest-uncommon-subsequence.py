class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        # if len(a) != len(b):
        #     return max(len(a),len(b))
        # s = 0
        # for i in range(len(a)):
        #     if a[i] != b[i]:
        #         s+=1
        # if s > 0:
        #     return s
        # return -1
        if a == b:
            return -1
        return max(len(a),len(b))
