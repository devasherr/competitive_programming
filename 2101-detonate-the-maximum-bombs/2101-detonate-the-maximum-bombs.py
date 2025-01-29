class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        res = 0
        n = len(bombs)

        for i in range(n):
            visited = set([i])
            count = 1
            q = deque([bombs[i]])

            while q:
                x0, y0, radius = q.popleft()
                for j in range(n):
                    if j in visited:
                        continue

                    x1, y1 = bombs[j][0], bombs[j][1]
                    # formula to find distance between two points
                    d = ((x1-x0)**2 + (y1-y0)**2) ** 0.5
                    if d <= radius:
                        q.append(bombs[j])
                        visited.add(j)
                        count += 1

            res = max(res ,count)
        return res 