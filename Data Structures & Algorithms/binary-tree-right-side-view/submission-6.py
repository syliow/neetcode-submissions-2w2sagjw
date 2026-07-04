# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # keyword: top to btm
        # pattern: bfs (lvl by lvl)
        #base case
        if not root:
            return []
        q = deque()
        q.append(root)
        res = []

        while q:
            lvl = len(q)
            curLvl = []
            for _ in range(lvl):
                node = q.popleft()
                curLvl.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(curLvl[-1])

        return res
