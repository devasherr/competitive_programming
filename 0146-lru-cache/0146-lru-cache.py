class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = self.right = None

class LRUCache:
    def __init__(self, capacity: int):
        # map key to node
        self.cacheMap = {}
        self.cap = capacity

        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)

        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    def get(self, key: int) -> int:
        if key in self.cacheMap:
            # update visited node to most recently used
            self.remove(self.cacheMap[key])
            self.insert(self.cacheMap[key])

            return self.cacheMap[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cacheMap:
            self.remove(self.cacheMap[key])

        self.cacheMap[key] = ListNode(key,value)
        self.insert(self.cacheMap[key])

        # if capacity passed remove from the left
        if len(self.cacheMap) > self.cap:
            LRU = self.left.next
            self.remove(LRU)
            del self.cacheMap[LRU.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)