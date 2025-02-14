class ProductOfNumbers:

    def __init__(self):
        self.arr = deque()     

    def add(self, num: int) -> None:
        if num == 0:
            self.arr = []
            return
        prev = self.arr[-1] if self.arr else 1
        self.arr.append(prev * num)

    def getProduct(self, k: int) -> int:
        if not self.arr: return 0
        
        left = self.arr[len(self.arr) - k - 1] if len(self.arr) - k - 1 >= 0 else 1
        if len(self.arr) < k:
            return 0
        return self.arr[-1] // left


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)