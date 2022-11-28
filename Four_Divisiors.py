class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            d = set()
            for i in range(1,math.floor(math.sqrt(n))+1):
                if n % i == 0:
                    d.add(n//i)
                    d.add(i)
                if len(d) > 4:
                    break
            if len(d) == 4:
                res += sum(d)
        return res
