class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        res, mx = 0, 0
        meetings.sort()
        print(meetings)

        for s, e in meetings:
            if s > days: break
            val = s - mx - 1
            if val > 0:
                res += val
            
            mx = max(mx, e)
        
        if mx < days:
            res += days - mx

        return res