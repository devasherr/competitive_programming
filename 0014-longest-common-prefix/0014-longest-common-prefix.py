class TrieNode:
    def __init__(self):
        self.children = {}
        
class Solution:
    def __init__(self):
        self.root = TrieNode()
        
    def longestCommonPrefix(self, strs: List[str]) -> str:
        index = len(strs[0])
        
        for word in strs:
            # insert every word into trie
            count = 0
            cur = self.root
            
            for c in word:
                if not cur.children:
                    cur.children[c] = TrieNode()
                elif c not in cur.children:
                    break
                cur = cur.children[c]
                count += 1
            index = min(index, count)
        
        return strs[0][:index]
                