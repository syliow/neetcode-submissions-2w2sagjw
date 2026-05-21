# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # dfs, set left to right, right to left
        # base case
        if not root:
            return None
        # swap
        root.left, root.right = root.right, root.left

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        return root
