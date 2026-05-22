# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # subroot cannot match an empty root
        if not root:
            return False

        if not subRoot:
            return True

        # matching subtree not enough
        # decendants also needs to match
        if self.isSametree(root, subRoot):
            return True

        # what if it doesnt matches directly? we need to dig deeper
        # it should be on either side
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSametree(self, root, subRoot):
        if not root and not subRoot:
            return True

        # need to match everything, dun care about decendant for now
        if root and subRoot and root.val == subRoot.val:
            return self.isSametree(root.left, subRoot.left) and self.isSametree(
                root.right, subRoot.right
            )
        else:
            return False
