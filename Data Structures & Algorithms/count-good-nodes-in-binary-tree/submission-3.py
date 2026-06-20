# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # pattern: DFS
        # good node = maxSeen <= node.val
        def dfs(node, maxSeen):
            # base case
            if not node:
                return 0
            if maxSeen <= node.val:
                goodNode = 1
            else:
                goodNode = 0
                
            maxSeen = max(maxSeen, node.val)
            goodNode += dfs(node.left, maxSeen)
            goodNode += dfs(node.right, maxSeen)
            return goodNode

        return dfs(root, root.val)
