class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def generate(i, cur, path):
            if cur > target: return
            if cur == target:
                res.append(path[:])
                return
            
            for j in range(i, len(candidates)):
                path.append(candidates[j])
                generate(j, cur+candidates[j], path)
                path.pop()

        generate(0, 0, [])
        return res