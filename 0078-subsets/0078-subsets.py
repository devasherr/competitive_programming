class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        # 1 2 3
        curSet = []
        def dfs(i):
            if i >= len(nums):
                res.append(curSet.copy())
                return 

            # decision to include
            curSet.append(nums[i])
            dfs(i + 1)

            # decision not to include
            curSet.pop()
            dfs(i + 1)

        dfs(0)

        return res