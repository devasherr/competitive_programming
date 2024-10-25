class TrieNode:
    def __init__(self):
        self.children = {}
        self.val = 0

class MapSum:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        cur = self.root
        for c in key:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.val = val

    def sum(self, prefix: str) -> int:
        res = 0
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return 0
            cur = cur.children[c]
        res += self.recursiveSum(cur, 0)
        return res

    def recursiveSum(self, cur, total):
        total += cur.val
        if not cur.children:
            return total

        result = 0
        for child in cur.children.values():
            result += self.recursiveSum(child, total)
        return result

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)