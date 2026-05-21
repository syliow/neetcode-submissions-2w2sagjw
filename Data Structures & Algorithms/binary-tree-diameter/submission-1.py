# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # use height to calculate diameter
        # dfs = return height
        # diameter = return diameter
        # pattern : dfs
        res = 0

        def dfs(node):
            nonlocal res

            if not node:
                return 0

            # to get diameter , we need height first
            # height formula = 1 + max(L, R)
            left = dfs(node.left)
            right = dfs(node.right)
            # diameter formula = max(diameter, left + right)
            res = max(res, left + right)

            return 1 + max(left, right)

        dfs(root)
        return res
