class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) ==  1:
            return 0
        
        q = deque([0])
        visited = set([0])
        jumps, found = 0, False

        while q:
            for _ in range(len(q)):
                idx = q.popleft()
                for i in range(nums[idx]):
                    nextIndex = idx+i+1
                    if nextIndex == len(nums) - 1:
                        found = True

                    if nextIndex not in visited:
                        q.append(nextIndex)
                        visited.add(nextIndex)
            jumps += 1
            if found:
                return jumps
            