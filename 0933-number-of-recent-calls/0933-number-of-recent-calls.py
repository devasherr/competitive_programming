class RecentCounter:

    def __init__(self):
        self.recent = []
        self.index = 0

    def ping(self, t: int) -> int:
        self.recent.append(t)

        while (t - 3000) > self.recent[self.index]:
            self.index += 1
        
        return len(self.recent) - self.index

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)