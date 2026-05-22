# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS: queue (FIFO)
        res = []
        q = deque()
        q.append(root)

        while q:
            qLen = len(q)
            # each node in current lvl
            level = []
            for i in range(qLen):
                # process each node in cur lvl
                node = q.popleft()
                if node:
                    level.append(node.val)  # push to cur lvl
                    q.append(node.left)
                    q.append(node.right)
                # only push to res if lvl has something inside
            if level:
                res.append(level)
        return res
