"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        # pattern: use dict to store ori -> copy
        # build a new list using ref from old copy
        # dfs visited
        cloneMap = {}

        def dfs(node):
            # base case
            if not node:
                return None
            if node in cloneMap:
                return cloneMap[node]

            copy = Node(node.val)
            cloneMap[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node)
