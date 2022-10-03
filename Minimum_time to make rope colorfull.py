class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        n=len(s)
        res = 0
        max_time = cost[0]
        full_time = cost[0]
        size = 1
        color= s[0]

        for i in range(1,n):
            cur_color = s[i]
            if cur_color == color:
                size  += 1 
                full_time += cost[i]
                max_time = max(max_time , cost[i])
            else:
                res += full_time - max_time
                color = cur_color
                max_time = cost[i]
                full_time = cost[i]
                size = 1
            if i == n-1:
                if size != 1:
                    res += full_time - max_time
        return (res)
