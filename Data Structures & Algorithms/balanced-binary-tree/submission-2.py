# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # height = count down to lowest node = dfs
        def dfs(node):
            # base case
            if not node:
                return [0, True]  # [height, isBalanced]
            left = dfs(node.left)
            right = dfs(node.right)
            isBalanced = left[1] and right[1] and abs(left[0] - right[0]) <= 1
            height = 1 + max(left[0], right[0])  # get the deepest height
            return [height, isBalanced]

        return dfs(root)[1]
