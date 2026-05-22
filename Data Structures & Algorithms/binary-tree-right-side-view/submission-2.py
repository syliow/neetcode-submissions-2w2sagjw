# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # pattern: BFS, queue
        if not root:
            return []

        res = []
        q = deque()
        q.append(root)
        # core idea: push every node from L -> R , R will always at last
        while q:
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()  # pop removes last item (right side)

                if i == qLen - 1:
                    res.append(node.val)
                # q handle tracking future nodes

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

        return res
