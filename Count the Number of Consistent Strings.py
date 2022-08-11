class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s = 0
        a = set(allowed)
        # print(a)
        for i in range(len(words)):
            t = set(words[i])
        #     print(t)
            if not (t-a):
        #         print(t-a)
                s +=1
        return s
