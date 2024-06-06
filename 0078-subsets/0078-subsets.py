class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        curSet = []
        def dfs(i):
            if i >= len(nums):
                res.append(curSet.copy())
                return

            curSet.append(nums[i])
            dfs(i + 1)

            curSet.pop()
            dfs(i + 1)

        dfs(0)
        return res