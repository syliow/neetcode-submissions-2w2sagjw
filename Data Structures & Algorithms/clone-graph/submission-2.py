"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        nodeMap = {}

        def dfs(node):
            # base case
            if not node:
                return None

            if node in nodeMap:
                return nodeMap.get(node)
            # if not in map, create a clone and store in map
            copy = Node(node.val)
            nodeMap[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node)
