# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            # base case
            # both missing = same
            if not p and not q:
                return True

            # cannot miss either one
            if not p or not q:
                return False

            # if both p and q present
            if p and q and p.val == q.val:
                # now go to their child
                left = dfs(p.left, q.left)
                right = dfs(p.right, q.right)
                return left and right
            else:
                # if p and q present but p.val != q.val
                return False

        return dfs(p, q)
