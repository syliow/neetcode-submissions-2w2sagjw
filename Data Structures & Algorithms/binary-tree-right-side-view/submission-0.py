# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque([root])

        while q:
            rightSide = None
            qLen = len(q) #every node in the current lvl

            for i in range(qLen):
                node = q.popleft()
                #go through every node in the curr lvl
                if node:
                    #process from L -> R
                    #last node val is always the R val
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
                
            if rightSide:
                res.append(rightSide.val)
        return res
