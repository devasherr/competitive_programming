class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextMap = defaultdict(lambda: -1)
        res = []
        
        for i in range(len(nums2)):
            for j in range(i, len(nums2)):
                if nums2[j] > nums2[i]:
                    nextMap[nums2[i]] = nums2[j]
                    break

        for n in nums1:
            res.append(nextMap[n])

        return res