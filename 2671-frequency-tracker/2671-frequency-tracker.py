class FrequencyTracker:

    def __init__(self):
        self.container = defaultdict(int)
        self.freq = defaultdict(int)        

    def add(self, number: int) -> None:
        self.container[number] += 1
        self.freq[self.container[number]] += 1
        self.freq[self.container[number] - 1] -= 1

    def deleteOne(self, number: int) -> None:
        if self.container[number]:
            self.container[number] -= 1
            if self.container[number] == 0:
                del self.container[number]

            self.freq[self.container[number]] += 1
            self.freq[self.container[number] + 1] -= 1

    def hasFrequency(self, frequency: int) -> bool:
        if frequency in self.freq and self.freq[frequency] > 0:
            return True
        return False


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)