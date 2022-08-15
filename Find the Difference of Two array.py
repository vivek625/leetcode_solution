# Vivek Raj Singh
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        d = set(nums1)
        e = set(nums2)
        dd= (list(d-e))
        ee= (list(e-d))
        s = []
        s.append(dd)
        s.append(ee)
        return (s)
