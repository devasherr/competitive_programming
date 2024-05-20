class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            dfs(i+1)

        dfs(0)

        def calcXOR(nums):
            cur = 0
            for n in nums:
                cur ^= n
            return cur

        ans = 0
        for lst in res:
            ans += calcXOR(lst)

        return ans