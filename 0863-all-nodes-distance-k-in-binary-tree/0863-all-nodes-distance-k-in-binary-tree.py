# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # construct the graph
        q = deque([root])
        graph = defaultdict(list)

        while q:
            node = q.popleft()

            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                q.append(node.left)

            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.val].append(node.right.val)
                q.append(node.right)
        
        # bfs by level
        q = deque([target.val])
        visited = set([target.val])
        depth = 0

        while q:
            if depth == k:
                break

            for _ in range(len(q)):
                cur = q.popleft()

                for nei in graph[cur]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)
            depth += 1

        return list(q)