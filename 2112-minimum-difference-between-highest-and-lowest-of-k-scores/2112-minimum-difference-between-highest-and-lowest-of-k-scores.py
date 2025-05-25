class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        q = deque()
        res = float("inf")

        for n in nums:
            q.append(n)
            if len(q) == k:
                res = min(res, q[-1] - q[0])
                q.popleft()
        
        return res if res != float("inf") else 0