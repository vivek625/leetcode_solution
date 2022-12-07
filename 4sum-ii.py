class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
#         --------------------------------------------------------------------------------------------------------------------
        # s= []
        # nums11 = list(set(nums1));nums22 = list(set(nums2));nums33 = list(set(nums3)) ; nums44 = list(set(nums4))
        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):
        #         for k in range(len(nums3)):
        #             for l in range(len(nums4)):
        #                 if (nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0):
        #                     s.append({nums1[i],nums2[j],nums3[k],nums4[l]})
        # return(len(s))
#         ---------------------------------------------------------------------------------------------------------------------------------
        from Collection import Counter
        s = Counter(i+j for i in nums1 for j in nums2 )
        n = sum(s[-k-l] for k in nums3 for l in nums4)
        return n
