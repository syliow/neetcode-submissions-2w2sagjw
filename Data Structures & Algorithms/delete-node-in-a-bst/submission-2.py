class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        # Step 1: Search for the node
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)

        # Step 2: Delete the node (when found)
        else:
            # Case 1: No left child
            if not root.left:
                return root.right

            # Case 2: No right child
            elif not root.right:
                return root.left

            # Case 3: Both children exist
            else:
                # Find smallest node in right subtree
                cur = root.right
                while cur.left:
                    cur = cur.left

                # Replace current node's value with smallest value
                cur.left = root.left
                res = root.right
                del root
                return res

        return root
