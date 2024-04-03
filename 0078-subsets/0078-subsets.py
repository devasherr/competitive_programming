class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        # recursive backtracking
        def tracker(i):
            if i >= len(nums):
                res.append(subset.copy())
                return 
            
            # decide to include
            subset.append(nums[i])
            tracker(i + 1)

            # decide NOT to inculde
            subset.pop()
            tracker(i + 1)
        
        # call function of first index (0)
        tracker(0)

        return res