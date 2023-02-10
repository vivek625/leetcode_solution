class Solution:
    def smallestNumber(self, num: int) -> int:
        # num1 = str(num)
        # s =[]
        # if num1[0] == '-':
        #     k = '-'
        #     num1 = num1[1:]
        #     p = (max([((''.join(i))) for i in permutations(num1)]))
        #     return int(k+p)
        # else:
        #     p = (([((''.join(i))) for i in permutations(num1)]))
        #     for i in p:
        #         if i[0] == '0':
        #             i = i[1:]
        #             pass
        #         else:
        #             s.append(int(i))
        # return min(s)


        num1 = sorted(str(abs(num)))
        if num <= 0:
            k = "".join(num1)
            ans = k[::-1]
            return(-int(ans))
        # if num1[0] == '0':
        #     num1[0] , num1[1] = num1[1],num1[0]
        #     k = (''.join(num1))
        #     return (int(k))
        for i , num in enumerate(num1):
            if num > '0':
                num1[i] , num1[0] = num1[0] , num1[i]
                k = (''.join(num1))
                return int(k)
        k = ("".join(num1))
        return int(k)
