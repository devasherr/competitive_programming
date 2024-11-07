class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        n = len(candidates)

        def dp(i, cur, count):
            if i == n: return count
            
            if (i, cur, count) in memo:
                return memo[(i, cur, count)]

            temp = cur & candidates[i]
            val = count + 1 if temp > 0 else count

            include = dp(i+1, temp, val)
            exclude = dp(i+1, cur, count)

            memo[(i, cur, count)] = max(include, exclude)
            return memo[(i, cur, count)]
        
        memo = {}
        return dp(0, candidates[0], 0)