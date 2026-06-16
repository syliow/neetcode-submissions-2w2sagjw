# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # base case
        if not root:
            return []
        # pattern: bfs
        q = deque()
        # push root to q
        q.append(root)
        res = []
        while q:
            lvl = len(q)
            depth = []
            for _ in range(lvl):
                node = q.popleft()
                depth.append(node.val)
                # continue push
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(depth[-1])
        return res
