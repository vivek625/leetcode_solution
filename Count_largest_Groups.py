class Solution:
    def countLargestGroup(self, n: int) -> int:
        counter = Counter()
        k = []
        for i in range(1,n+1):
            counter[sum(int(j) for j in str(i))] += 1
        l = Counter(counter.values())
        # print(l)
                
        return (l[max(l)])
