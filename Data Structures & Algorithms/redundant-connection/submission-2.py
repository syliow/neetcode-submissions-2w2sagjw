class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # pattern: detect cycle -> DFS
        adj = defaultdict(list)

        def dfs(node, target, visited):
            # we need prev to not false flag theres cycle
            # base case: path already exists
            if node == target:
                return True
            visited.add(node)
            # go through neighbor
            for nei in adj[node]:
                if nei in visited:
                    continue
                # if no detect cycle
                if dfs(nei, target, visited):
                    return True
            return False

        for u, v in edges:
            # if u and v is connected, add this edge = cycle
            if dfs(u, v, set()):
                return [u, v]
            # add edge to graph, no cycle
            adj[u].append(v)
            adj[v].append(u)
        return []
