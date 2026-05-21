# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # height balanced , L and R height must be <= 1
        # go down deepest , then come up with height
        # [isBalanced, height]
        # since we need to get height, dfs makes sense to go deepest

        def dfs(node):
            # base case
            if not node:
                return [True, 0]  # empty tree is balanced

            # height
            left = dfs(node.left)
            right = dfs(node.right)
            isBalanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            # height = 1(parent) + max(left, right)
            return [isBalanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]
