# class Solution:
#     def isHappy(self, n: int) -> bool:
#         n_hash = set()
#         while n:
#             if n == 1:
#                 return True
#             if n in n_hash:
#                 return False
#             else:
#                 n_hash.add(n)
#                 n = self.sum_squared_digits(n)
                
#     def sum_squared_digits(self, n: int) -> int:
#         sum_dig = 0
#         while n:
#             digit = n % 10
#             sum_dig += digit ** 2    
#             n = n // 10
#         return sum_dig

class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        # s = 0
        while n:
            if n == 1:
                return True
            if n in s:
                return False
            else:
                s.add(n)
                n = self.sum_sqrt(n)
    def sum_sqrt(self,n:int)->int:
        sd = 0
        while n:
            digit = n % 10
            sd += digit**2
            n = n // 10
        return sd
        
