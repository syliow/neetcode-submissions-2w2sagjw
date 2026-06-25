# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # pattern: postorder L -> R -> Root
        res = []

        def dfs(node):
            # base case
            if not node:
                return None
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)

        dfs(root)
        return res
