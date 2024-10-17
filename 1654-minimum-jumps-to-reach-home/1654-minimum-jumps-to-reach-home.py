class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        q = deque([[0, 0]])
        upperbound = max(max(forbidden), x) + a + b
        forbidden = set(forbidden)
        visit = set([0])

        level = 0
        while q:
            for _ in range(len(q)):
                y, direction = q.popleft()
                if x == y:
                    return level

                # forward
                if y + a not in visit and y + a not in forbidden and y + a < upperbound:
                    q.append((y+a, 1))
                    visit.add(y+a)

                # backward
                if direction != -1 and y - b >= 0 and y - b not in visit and y - b not in forbidden:
                    q.append((y-b, -1))
                    visit.add(y-b)
            level +=1
        
        return -1