class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # this has duplicates
        res, cur = [], []

        def backtrack(i, total):
            if total >= target:
                if total == target:
                    res.append(cur[:])
                return

            for idx in range(len(candidates)):
                cur.append(candidates[idx])
                backtrack(idx, sum(cur))
                cur.pop()

        backtrack(0, 0)
        return res