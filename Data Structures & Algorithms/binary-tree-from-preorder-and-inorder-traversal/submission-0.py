# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder or not inorder:
            return None
        #first val in preorder
        root = TreeNode(preorder[0])
        #split the tree into L and R section
        mid = inorder.index(preorder[0])
        #core idea: preorder(root - L - R) ; inorder(L - Root(mid) - R)
        #[start:end]
        root.left = self.buildTree(preorder[1: mid + 1], inorder[0:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root