class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        remaning = k
        for i in range(k):
            if chalk[i % len(chalk)] > remaning:
                return i % len(chalk)

            remaning -= chalk[i % len(chalk)]