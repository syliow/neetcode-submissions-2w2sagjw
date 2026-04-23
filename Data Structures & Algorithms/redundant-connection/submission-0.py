class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]

        def dfs(node, par, visit):
            visit.add(node)
        
            for nei in adj[node]:
                if nei == par:
                    continue
                if nei in visit:
                    return True
                if dfs(nei, node, visit):
                    return True
            return False

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

            if dfs(u, -1, set()):
                return [u, v]
        return []