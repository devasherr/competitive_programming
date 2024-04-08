class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix = [0] * n

        for book in bookings:
            first, last , seat = book[0], book[1], book[2]

            prefix[first - 1] += seat
            if last < n:
                prefix[last] -= seat 
        
        i = 1
        while i < n:
            prefix[i] += prefix[i - 1]
            i += 1
        
        return prefix