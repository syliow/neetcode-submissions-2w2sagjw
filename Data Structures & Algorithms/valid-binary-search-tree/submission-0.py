class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
       #core idea: valid BST = L < Root, R > Root 

       def valid(node, left, right):
            if not node: #even no node = valid
                return True
            #check for core idea above
            if not (left < node.val < right):
                return False

            #recursion (L and R)
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
            
       return valid(root, float("-inf"), float("inf"))