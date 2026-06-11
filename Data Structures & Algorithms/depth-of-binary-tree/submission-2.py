# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #find depth, pattern = dfs to go deepest
        #idea: go deepest and comeback to get depth count

        def dfs(node):
            #base case: null = 0 depth
            if not node:
                return 0
            #for every depth we go down, we + 1
            left = 1 + dfs(node.left)
            right = 1 + dfs(node.right)
            return max(left, right)
        return dfs(root)