# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, minVal, maxVal):
            # base case
            if not node:
                return True
            # everything on left needs to be < maxVal
            # everything on right needs to be > maxVal
            if not minVal < node.val < maxVal:
                return False
            # check for L R subtree
            left = dfs(node.left, minVal, node.val)
            right = dfs(node.right, node.val, maxVal)
            return left and right

        return dfs(root, float("-inf"), float("inf"))
