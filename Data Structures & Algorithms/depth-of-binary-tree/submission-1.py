# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        #explanation: we go to deepest, +1 for every depth we pass thru
        #we check L, R bcs each side might not be equal
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
