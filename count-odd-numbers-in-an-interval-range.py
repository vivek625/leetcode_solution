class Solution:
    def countOdds(self, low: int, high: int) -> int:
    #-------------------------------------------------------------------------------
        # s =[]
        # for i in range(low,high+1):
        #     if i % 2 != 0:
        #         s.append(i)
        # return len(s)
     #---------------------------------------------------------------------------------
        # return len( [ i for i in range(low,high+1) if i % 2 != 0])
      # --------------------------------------------------------------------------------
        # s = 0
        # for i in range(low,high+1):
        #     if i % 2 != 0:
        #         s += 1
        #     pass
        # return s
        #------------------------------------------------------------------------------
        return (high - low ) //2 + (high % 2 or low % 2)