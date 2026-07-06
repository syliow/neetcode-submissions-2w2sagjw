class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        
        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append((b, values[i]))
            adj[b].append((a, 1/ values[i]))

        def dfs(src, target, visited):
            #base case: success
            if src == target:
                return 1.0
            visited.add(src)

            for nei, weight in adj[src]:
                if nei not in visited:
                    result = dfs(nei, target, visited)
                    if result != -1:
                        return weight * result
            return -1.0

        res = []
        for c, d in queries:
            #both must exist in graph
            if c not in adj or d not in adj:
                res.append(-1.0)
            else:
                res.append(dfs(c, d, set()))
        return res