class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # adj list = map each node to neighbors
        # Eg:
        # [
        #     [1, 2, 3], #Node 0 is connected to 1 2 3
        #     [0, 2], #Node 1 is connected to 0 2
        #     [0] #Node 3 is connected to 0
        # ]
        visited = set()
        # base case:
        # no cycle + have n - 1 edges
        if len(edges) > n - 1:
            return False

        adj = [[] for _ in range(n)]
        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)

        def dfs(node, prev):
            # cycle detected
            if node in visited:
                return False

            visited.add(node)
            # go thru each nei
            for nei in adj[node]:
                # ignore from prev val
                if nei == prev:
                    continue
                # no cycle
                if not dfs(nei, node):
                    return False
            return True

        # use -1 as placeholder for root prev val
        # len of n must be == visit length
        return dfs(0, -1) and len(visited) == n
