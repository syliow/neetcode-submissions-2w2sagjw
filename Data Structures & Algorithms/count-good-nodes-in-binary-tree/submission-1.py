# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Good nodes = maxNum <= node.val
        # pattern: DFS
        def dfs(node, maxNum):
            # base case
            if not node:
                return 0
            # good node check
            if maxNum <= node.val:
                res = 1
            else:
                res = 0

            maxNum = max(maxNum, node.val)  # update maxnum
            res += dfs(node.left, maxNum)
            res += dfs(node.right, maxNum)
            return res

        return dfs(root, root.val)
