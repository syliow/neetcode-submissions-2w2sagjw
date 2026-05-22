# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder: Root -> L -> R (root in pre)
        # inorder: L -> Root -> R (root in mid)
        # preorder = [1 (Root),2 (L),3,4], inorder = [2 (L),1 (Root),3,4]

        # if arr empty, no tree to build
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        midIndex = inorder.index(preorder[0])

        root.left = self.buildTree(
            # left preorder
            preorder[1 : midIndex + 1],
            # left inorder
            inorder[0:midIndex],
        )

        root.right = self.buildTree(
            # right preorder
            preorder[midIndex + 1 :],  # everything after mid
            # right inorder
            inorder[midIndex + 1 :],  # everything after mid
        )

        return root
