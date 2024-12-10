class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        bads = []
        for i in range(1, len(nums)):
            if nums[i] % 2 == nums[i-1] % 2:
                bads.append(i)
        
        def binarySearch(f, t):
            good = True
            left, right = 0, len(bads) - 1
            while left <= right:
                mid =  (left + right) // 2
                if bads[mid] > t:
                    right = mid - 1
                elif bads[mid] <= f:
                    left = mid + 1
                else:
                    good = False
                    break
            return good

        res = []
        for f, t in queries:
            res.append(binarySearch(f, t))
        return res