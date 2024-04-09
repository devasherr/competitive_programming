class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        target = tickets[k]

        for i in range(len(tickets)):
            tickets[i] -= target
        
        firstOut = min(tickets)

        for n in tickets:
            if n >= 0:
                res += target
            else:
                res += (target + firstOut)
        return res