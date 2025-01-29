class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        res = 0
        def connected_points(x1, y1, x2, y2, d1):
            dist = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5
            return dist <= d1

        for i in range(len(bombs)):
            q = deque([i])
            visit = set([i])
            count = 1

            while q:
                idx = q.popleft()
                x1, y1, d1 = bombs[idx]
                for j in range(len(bombs)):
                    if j in visit: continue
                    x2, y2, d2 = bombs[j]

                    if connected_points(x1, y1, x2, y2, d1):
                        count += 1
                        q.append(j)
                        visit.add(j)
            
            res = max(res, count)
        return res