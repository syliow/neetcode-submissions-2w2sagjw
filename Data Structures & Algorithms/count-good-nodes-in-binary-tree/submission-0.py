# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #good node = from root to that node, all val < node.val
        #key idea: carry max val seen for path
        #curr node val >= max , good node

        def dfs(node, maxVal):
            if not node:
                return 0
                
            if node.val >= maxVal:
                res = 1
            else: 
                res = 0
            
            maxVal = max(maxVal, node.val)
            #recursion 
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res

        return dfs(root, root.val)
