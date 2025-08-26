class TrieNode:
    def __init__(self, val):
        self.val = val
        self.child = {}
        self.isLast = False

class Trie:
    def __init__(self): 
        self.root = TrieNode(-1)

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.child:
                cur.child[c] = TrieNode(c)
            cur = cur.child[c]
        cur.isLast = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.child: return False
            cur = cur.child[c]
        return cur.isLast

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.child: return False
            cur = cur.child[c]
        return True
