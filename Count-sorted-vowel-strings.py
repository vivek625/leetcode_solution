class Solution:
    def countVowelStrings(self, n: int) -> int:
        # n = 1
        s = ['a', 'e', 'i', 'o', 'u']
        # ans = []
        # perm = permutations(s,n)
        # for i in (perm):
        #     ans.append(tuple(set(i)))
        # if n == 1:
        #     return len(set(ans))
        # else:
        #     return len(set(ans))+5
        return ((n+1)*(n+2)*(n+3)*(n+4)//24)
