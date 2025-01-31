class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        res = float("inf")
        for ghost in ghosts:
            res = min(res, abs(target[0] - ghost[0]) + abs(target[1] - ghost[1]))
        return abs(target[0]) + abs(target[1]) < res