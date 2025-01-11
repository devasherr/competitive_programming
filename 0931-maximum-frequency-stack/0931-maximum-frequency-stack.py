class FreqStack:

    def __init__(self):
        self.countsMap = defaultdict(list)
        self.count = defaultdict(int)
        self.top = 0

    def push(self, val: int) -> None:
        self.count[val] += 1
        self.countsMap[self.count[val]].append(val)
        self.top = max(self.top, self.count[val])

    def pop(self) -> int:
        num = self.countsMap[self.top].pop()
        self.count[num] -= 1
        if not self.countsMap[self.top]:
            self.top -= 1
        return num

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()