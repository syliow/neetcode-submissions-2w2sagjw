class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # adj list
        # dfs
        # res = count of components
        adj = [[] for _ in range(n)]
        visited = set()
        res = 0

        # [[0]: add 0 neighbors here]
        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)

        def dfs(node):
            # base case
            for nei in adj[node]:
                # continue dfs if its not visited
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)

        for node in range(n):
            # only proceed if not visited
            if node not in visited:
                visited.add(node)
                dfs(node)
                res += 1

        return res
