class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums1, nums2, nums3 = set(nums1), set(nums2), set(nums3)
        count = defaultdict(int)

        for n in nums1:
            count[n] += 1
        for n in nums2:
            count[n] += 1
        for n in nums3:
            count[n] += 1
        
        res = []
        for key in count:
            if count[key] > 1:
                res.append(key)
        
        return res