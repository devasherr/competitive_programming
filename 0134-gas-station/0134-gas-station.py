class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        for i in range(n):
            # go around the circle
            count, tank = 0, 0
            j = i

            while True:
                if count == n:
                    return i
                tank += gas[j]

                if tank < cost[j]:
                    break
                tank -= cost[j]
                j = (j + 1) % n
                count += 1

        return -1    