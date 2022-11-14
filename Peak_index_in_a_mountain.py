class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        s = max(arr)
        for i in range(len(arr)):
            if arr[i] == s:
                return i
