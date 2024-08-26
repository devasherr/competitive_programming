class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n = len(nums1)
        i, j = 0, 0
        res = []

        while i < n and j < n and k:
            n1 = nums1[i] + nums2[j]
            n2 = nums1[i+1] + nums2[j] if i + 1 < n else nums1[i] + nums2[j]

            if n1 < n2:
                res.append([nums1[i], nums2[j]])
                j += 1
            else:
                if i + 1 < n:
                    res.append([nums1[i+1], nums2[j]])
                else:
                    res.append([nums1[i], nums2[j]])
                i += 1

            k -= 1
        
        return res