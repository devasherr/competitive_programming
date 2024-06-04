class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i+1 for i in range(n)]
        res, cur = [], []

        def backtrack(i, k):
            if i >= len(nums) or len(cur) == k:
                if len(cur) == k:
                    res.append(cur.copy())
                return
         
            cur.append(nums[i])
            backtrack(i+1, k)
            cur.pop()
            backtrack(i+1, k)

        backtrack(0, k)
        return res