class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t: t[1])

        # [end, num of passengers]
        minHeap = []
        curPass = 0 

        for trip in trips:
            numPass, start, end = trip

            while minHeap and minHeap[0][0] <= start:
                curPass -= minHeap[0][0]
                heapq.heappop(minHeap)
            
            curPass += numPass
            if curPass > capacity:
                return False
            heapq.heappush(minHeap, [end, numPass])

        return True