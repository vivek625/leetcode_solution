class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        k = []
        ans = 0
        for i in range(len(bank)):
            s = 0
            for j in range(len(bank[0])):
                if bank[i][j] == '1':
                    s +=1
            if s == 0:
                pass
            else:
                k.append(s)
        for i in range(len(k)-1):
            ans +=( k[i] * k[i+1])
        return (ans)  
