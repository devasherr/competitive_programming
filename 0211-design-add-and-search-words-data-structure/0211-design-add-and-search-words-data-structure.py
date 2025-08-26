class TrieNode():
    def __init__(self, val):
        self.val = val
        self.child = {}
        self.isLast = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode("")

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.child:
                cur.child[c] = TrieNode(c)
            cur = cur.child[c]
        cur.isLast = True

    def search(self, word: str) -> bool:
        def _search(word, cur):
            if not word: return cur.isLast
            if word[0] != "." and word[0] not in cur.child: return False

            if word[0] == ".":
                found = False
                for tree in cur.child.values():
                    found |= _search(word[1:], tree)
                return found
            else:
                return _search(word[1:], cur.child[word[0]])

        cur = self.root
        return _search(word, cur)
