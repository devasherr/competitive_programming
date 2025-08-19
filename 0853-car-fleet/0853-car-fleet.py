class Solution:
    def carFleet(self, target, position, speed) -> int:
        cars = [(target - p) / s for p, s in sorted(zip(position, speed))]
        for i in range(len(cars)-2, -1, -1):
            cars[i] = max(cars[i], cars[i+1])
        return len(set(cars))
