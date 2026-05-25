class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]

        # dfs
        def dfs(node, prev):
            if node in visited:
                return True
            visited.add(node)
            for nei in adj[node]:
                if nei == prev:
                    continue
                # if no detect cycle = return true
                if dfs(nei, node):
                    return True
            return False

        # process node 1 by 1
        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)

            visited = set()

            # if DFS returns True,
            # it means exploring from node1 hit a cycle
            if dfs(node1, -1):
                return [node1, node2]

        return []
