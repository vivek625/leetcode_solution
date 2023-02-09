class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # s =[]
        # nums1 = list(set(nums1))
        # nums2 = list(set(nums2))
        # nums1.sort()
        # nums2.sort()
        # l = min(len(nums1),len(nums2))
        # for i in nums1:
        #     if i in nums2:
        #         return i
        # return -1


        s = set(nums2)
        nums1.sort()
        for i in nums1:
            if i in s:
                return i
        return -1
