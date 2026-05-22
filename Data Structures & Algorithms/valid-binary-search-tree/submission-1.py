# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #BST core logic: left.val < node.val < right.val

        # min: - inf , max: inf
        def dfs(node, min, max):
            # base case: empty node = valid BST
            if not node:
                return True

            # check for invalid BST constraints:
            if not min < node.val < max:
                return False

            # L = node.val = new max
            left = dfs(node.left, min, node.val)
            # R = node.val = new min
            right = dfs(node.right, node.val, max)
            
            return left and right

        return dfs(root, float("-inf"), float("inf"))
