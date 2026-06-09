# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #pattern: bfs, level by level . L -> R
        #base case
        if not root:
            return []
        res = []
        q = deque()
        q.append(root)
        #issue: how to determine lvl
        #base case: empty node
        while q:
            qLength = len(q)
            lvl = []
            for _ in range(qLength):
                node = q.popleft()
                lvl.append(node.val)
                    #repeat for L and R
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(lvl)
                
        return res
