# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # pattern: go as deep as possible = dfs
        # inorder: L -> Root -> R
        # res: store nodes in ascending order
        # return arr in kth (1 indexed)
        res = []

        def dfs(node):
            # base case
            if not node:
                return None

            # L -> Root -> R
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)

        dfs(root)
        return res[k - 1]
