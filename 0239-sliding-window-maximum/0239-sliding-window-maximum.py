class Solution:
    def maxSlidingWindow(self, nums, k: int):
        q = deque()
        res = []
        left = 0

        for right in range(len(nums)):
            while q and nums[right] > q[-1]:
                q.pop()

            q.append(nums[right])
            if right - left + 1 < k: continue

            res.append(q[0])
            if q and q[0] == nums[left]:
                q.popleft()
            left += 1

        return res
