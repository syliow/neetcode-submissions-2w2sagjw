class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # pattern: recursion dfs
        # idea: check is all edges connected as a valid tree
        # detect cycle
        if len(edges) > n - 1:
            return False
        # adj list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        # [[1, 2, 3], [0, 4], [0], [0], [1]]
        # 0 -> nei: 1,2,3 ; 1 -> 0 and 4
        visited = set()

        def dfs(node, parent):
            # base case: cycle detected - return False
            if node in visited:
                return False
            # mark node as visited
            visited.add(node)

            # recursion
            # how to access neighbor?
            for nei in adj[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n
