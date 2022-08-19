class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        s = []
        for i in range(0, len(arr)):
            j = i+1
            if j < len(arr):
                s.append(max(arr[j:]))
            else:
                s.append(-1)
        return s
