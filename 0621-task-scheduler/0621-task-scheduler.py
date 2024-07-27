class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap = [-n for n in Counter(tasks).values()]
        heapq.heapify(maxHeap)

        time = 1
        q = deque([(heapq.heappop(maxHeap) + 1, time+n)])
        while q or maxHeap:
            time += 1
            if maxHeap:
                val = heapq.heappop(maxHeap) + 1
                if val != 0: q.append((val, time+n))
            while q and q[0][1] == time:
                val = q.popleft()
                heapq.heappush(maxHeap, val[0])
        return time