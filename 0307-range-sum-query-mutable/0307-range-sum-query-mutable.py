class NumArray:
    def __init__(self, nums):
        self.nums = nums
        self.segTree = [0 for _ in range(4*len(nums))]

        self.build(0, 0, len(self.nums)-1)

    def build(self, index, left, right):
        if left == right:
            self.segTree[index] = self.nums[left]
            return

        mid = (left + right) // 2
        self.build(2*index+1, left, mid)
        self.build(2*index+2, mid+1, right)

        self.segTree[index] = self.segTree[2*index+1] + self.segTree[2*index+2]

    def _update(self, node, left, right, index, newVal):
        if left == right:
            self.segTree[node] = newVal
            return

        mid = (left + right) // 2
        if index <= mid:
            self._update(2*node+1, left, mid, index, newVal)
        else:
            self._update(2*node+2, mid+1, right, index, newVal)

        self.segTree[node] = self.segTree[2*node+1] + self.segTree[2*node+2]

    def update(self, index: int, val: int) -> None:
        self.nums[index] = val

        self._update(0, 0, len(self.nums)-1, index, val)

    def query(self, index, left, right, query_left, query_right):
        if query_right < left or query_left > right: return 0

        if query_left <= left and query_right >= right:
            return self.segTree[index]

        mid = (left + right) // 2
    
        leftTree = self.query(2*index+1, left, mid, query_left, query_right)
        rightTree = self.query(2*index+2, mid+1, right, query_left, query_right)

        return leftTree + rightTree

    def sumRange(self, left: int, right: int) -> int:
        return self.query(0, 0, len(self.nums)-1, left, right)
