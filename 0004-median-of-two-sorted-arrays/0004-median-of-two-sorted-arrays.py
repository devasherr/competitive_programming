class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = [0, 0]
        p1, p2, = 0, 0
        sumLength = len(nums1) + len(nums2)

        while p1 + p2 < sumLength / 2 + 1:
            if p1 >= len(nums1):
                cand = nums2[p2]
                p2 += 1
            elif p2 >= len(nums2):
                cand = nums1[p1]
                p1 += 1
            elif nums1[p1] < nums2[p2]:
                cand = nums1[p1]
                p1 += 1
            else:
                cand = nums2[p2]
                p2 += 1
            
            res[0], res[1] = res[1], cand

        if sumLength % 2 == 0:
            return sum(res) / 2
        else:
            return res[0]