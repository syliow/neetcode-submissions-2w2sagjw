class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # valid tree = no cycle
        # we can use dfs to detect cycle
        # we need to create adj list, go through nei, with visited set
        adj = defaultdict(list)
        # undirected = goes both ways
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = set()

        def dfs(node, parent):
            visited.add(node)

            for nei in adj[node]:
                if nei == parent:
                    continue  # avoid false cycle
                if nei in visited:
                    return False  # cycle
                if nei not in visited:
                    if not dfs(nei, node):
                        return False  # return false as soon we found 1 cycle
            return True

        return dfs(0, -1) and len(visited) == n
