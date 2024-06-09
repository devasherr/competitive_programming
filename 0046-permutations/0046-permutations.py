class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        def exCur(nums, target):
            res = []
            for n in nums:
                if n == target:
                    continue
                res.append(n)
            return res
        
        res = []
        def backtrack(nums, cur):
            if len(cur) == N:
                res.append(cur[:])
                return 
            
            for n in nums:
                cur.append(n)
                backtrack(exCur(nums, n), cur)
                cur.pop()
        backtrack(nums, [])
        return res