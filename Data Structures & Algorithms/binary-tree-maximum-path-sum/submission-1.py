# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(node):
            # base case
            if not node:
                return 0

            # track leftmax and rightmax
            leftMax = dfs(node.left)
            rightMax = dfs(node.right)

            # node could have negative values
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # compare max sum if we split
            # root + L + R
            res[0] = max(res[0], node.val + leftMax + rightMax)

            #Cannot split twice; breaks path continuity
            return node.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]
