# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []  # [1, 2, 3]

        def dfs(node):
            # base case
            if not node:
                res.append("N")  # N -> null
                return
            # convert int -> str
            res.append(str(node.val))
            # inorder (L -> Root -> R) -> asc order
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # split string into arrays (seperated by ,)
        vals = data.split(",")
        self.i = 0  # counter to point our current index

        def dfs():
            # base case: if node is Null
            if vals[self.i] == "N":
                self.i += 1
                return None
            # create a node, convert str -> int
            node = TreeNode(int(vals[self.i]))
            # move pointer forward
            self.i += 1

            node.left = dfs()
            node.right = dfs()

            return node
        return dfs()
