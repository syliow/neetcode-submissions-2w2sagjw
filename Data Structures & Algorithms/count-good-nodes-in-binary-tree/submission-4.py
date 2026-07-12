# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # good node = maxVal < node.val
        self.res = 0  # total good nodes

        def dfs(node, maxVal):
            # base case
            if not node:
                return None
            # count good node
            if maxVal <= node.val:
                self.res += 1
            # double check maxVal
            maxNum = max(maxVal, node.val)
            # go L and R
            dfs(node.left, maxNum)
            dfs(node.right, maxNum)

        dfs(root, root.val)
        return self.res
