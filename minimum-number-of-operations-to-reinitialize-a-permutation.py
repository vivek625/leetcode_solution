class Solution:
    def reinitializePermutation(self, n: int) -> int:
        s = [i for i in range(n)]
        count = 0
        arr = [0]*n
        perm = s[:]

        while s != arr:
            for i in range(n):
                if i % 2 == 0:
                    arr[i] = perm[int(i/2)]
        #             print(arr[i])
                else:
                    arr[i] = perm[int(n/2 +(i-1)/2)]
            perm = arr[:]
            count +=1
        return (count) 
