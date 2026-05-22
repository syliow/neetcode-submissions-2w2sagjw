# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # pattern: bfs (queue)
        # BST core idea: left.val < node.val < right.val
        # just like dfs
        q = deque([(root, float("-inf"), float("inf"))])

        while q:
            node, leftLimit, rightLimit = q.popleft()

            # check invalid BST conditions
            if not leftLimit < node.val < rightLimit:
                return False

            if node.left:
                q.append((node.left, leftLimit, node.val))

            if node.right:
                q.append((node.right, node.val, rightLimit))

        return True 
