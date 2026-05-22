# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # BFS: Queue
        res = 0
        q = deque()
        q.append((root, root.val))  # node, maxNum

        while q:
            node, maxNum = q.popleft()
            if node.val >= maxNum:
                res += 1
            maxNum = max(maxNum, node.val)
            # push L R children to q
            if node.left:
                q.append((node.left, maxNum))
            if node.right:
                q.append((node.right, maxNum))
        return res
