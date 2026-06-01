class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # pattern: DFS (need to look through every edge)
        # craft an adjacent list
        adj = defaultdict(list)
        # undirected so we need to make it 2 way u <---- > v
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = set()
        res = 0

        def dfs(node):  # visit and mark everything connected to this node
            # base case
            if node in visited:
                return 0

            visited.add(node)
            # recursion
            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)

        # go through each node
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)
        return res
