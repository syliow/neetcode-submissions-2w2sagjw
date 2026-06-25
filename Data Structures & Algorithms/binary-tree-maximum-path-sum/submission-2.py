# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # pattern: dfs
        self.res = root.val

        def dfs(node):
            # base case
            if not node:
                return 0

            leftMax = dfs(node.left)
            rightMax = dfs(node.right)

            # double check bcs the value could be -
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            # root + L + R, compare max
            self.res = max(self.res, node.val + leftMax + rightMax)
            #Parent node: can only pick one side to avoid revisit
            return node.val + max(leftMax, rightMax)

        dfs(root)
        return self.res
