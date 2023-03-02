class Solution:
    def compress(self, chars: List[str]) -> int:
        '''char = "".join(chars)
        char = set(char)
        char = sorted("".join(char))
        ans = []
        res = ""
        for i in char:
            k = str(chars.count(i))
            res += (i)
            if k == str('1'):
                pass
            else:
                res+=(k)
        print(res)
        print((ans))
        for i in res:
            ans.append(i)
        chars[:] = ans'''
        # from itertools import groupby
        ans = []
        for key, group in groupby(chars):

            count = len(list(group))
            ans.append(key)
            if count > 1:
                ans.extend(list(str(count)))
        chars[:] = ans
