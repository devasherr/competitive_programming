# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        level = 0
        maxHeap = []

        q = deque([root])
        while q:
            cur = 0
            for _ in range(len(q)):
                node = q.popleft()
                cur += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            maxHeap.append(-cur)
            level += 1
        
        if level < k: return -1
        heapq.heapify(maxHeap)

        for _ in range(k-1):
            heapq.heappop(maxHeap)
        return heapq.heappop(maxHeap) * -1