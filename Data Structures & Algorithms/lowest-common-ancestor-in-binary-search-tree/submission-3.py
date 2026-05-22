# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # LCA: the point where it splits to both L and R
        # or it splits towards onyl one direction -> keep looking
        # node = LCA : current node you are standing on IS one of the targets

        # if both values are smaller than root -> go L
        # if both values are larger than root -> go R
        # root is LCA -> One goes left and one goes right (the split point)
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q) #search L
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q) #search R
        else:
            return root
