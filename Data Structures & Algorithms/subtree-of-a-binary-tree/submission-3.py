# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # base case
        if not root:
            return False
        # the subroot must exactly match the subroot in root / root itself
        # if root is subroot
        if self.isSametree(root, subRoot):
            return True
        # check subroot against L and R children
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        return left or right

    def isSametree(self, root, subRoot):
        if not root and not subRoot:
            return True
        if not root or not subRoot or root.val != subRoot.val:
            return False
        left = self.isSametree(root.left, subRoot.left)
        right = self.isSametree(root.right, subRoot.right)
        return left and right
