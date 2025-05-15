class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        stack = [] # nums, index
        for i in range(len(groups)):
            while stack and stack[-1][0] == groups[i]:
                stack.pop()
            stack.append((groups[i], i))
        
        res = []
        for i in range(len(stack)):
            res.append(words[stack[i][1]])

        return res
        