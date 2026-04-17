# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #core idea: inorder (L -> Root -> R)
        #all in L nodes, top nodes, R nodes. Then pop
        stack = []
        curr = root

        while stack or curr: #ensure we visit every lvl
            while curr: #ensure we go as deep as possible (Left)
                stack.append(curr) #push node to stack so we can revisit
                curr = curr.left

            #start pop when reach end of Left
            curr = stack.pop()
            
            k -= 1
            if k == 0: #the node we pop is exactly the kth smallest ele
                return curr.val
            #now visit right side and repeat again
            curr = curr.right