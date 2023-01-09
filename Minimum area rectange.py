class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        min_size = []
        visit = set()
        for x1,y1 in points:
            for x2,y2 in visit:
                if (x1,y2) in visit and (x2,y1) in visit:
                    size = abs(x2-x1) * abs(y2-y1)
                    min_size.append(size)
            visit.add((x1,y1))
        if len(min_size) == 0:
            return 0
        if len(min_size) == 1:
            return min_size[0]
        else:
            return min(min_size)
