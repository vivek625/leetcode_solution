class Solution:
    def countPoints(self, rings: str) -> int:
        s = 0
        for i in range(10):
            i  = str(i)
            if 'B'+i in rings and 'R'+i in rings and 'G'+i in rings:
                s += 1
        return s
