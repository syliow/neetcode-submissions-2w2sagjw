class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        res = 0
        visited = set()
        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)

        def dfs(node):
            # base case
            for nei in adj[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)  # continue loop on nei

        # core idea: dfs
        # add , dfs
        for node in range(n):
            if node not in visited:
                visited.add(node)
                dfs(node)
                res += 1
        return res
