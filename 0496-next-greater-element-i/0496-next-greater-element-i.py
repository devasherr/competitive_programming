class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextNum = float("-inf")
        nextMap = {}

        for i in range(len(nums2) - 1, - 1, -1):
            if nums2[i] < nextNum:
                nextMap[nums2[i]] = nextNum
            else:
                nextMap[nums2[i]] = -1
            
            nextNum = nums2[i]

        res = []

        for n in nums1:
            res.append(nextMap[n])
        
        return res