class OrderedStream:
    def __init__(self, n: int):
        self.arr = [None] * n
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        # arr is 0 indexed

        self.arr[idKey-1] = value
        res = []

        if self.ptr == idKey - 1:
            while self.ptr < len(self.arr) and self.arr[self.ptr] != None:
                res.append(self.arr[self.ptr])
                self.ptr += 1

        return res



# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)