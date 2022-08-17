class Solution:
    def minOperations(self, logs: List[str]) -> int:
        s = []
        for i in logs:
            if s:
                if i == '../':
                    s.pop()
                elif i == './':
                    pass
                else:
                    s.append(i)
            else:
                if i not in ('../','./'):
                    s.append(i)
        return (len(s))
