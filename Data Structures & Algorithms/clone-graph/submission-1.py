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
        # dfs start from root
        def dfs(node):
            # base case: if node is null
            if not node:
                return None

            if node in nodeMap:
                return nodeMap[node]
            # store ori nodes -> cloned nodes
            nodeMap[node] = Node(node.val)

            # recursively do it for all neighbors, add to clone neighbor list
            for n in node.neighbors:
                clonedNei = dfs(n)
                nodeMap[node].neighbors.append(clonedNei)
            #return cloned niehgbor from map
            return nodeMap[node]

        return dfs(node) #pass in ori but return cloned
