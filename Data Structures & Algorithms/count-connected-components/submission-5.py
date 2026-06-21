class Solution: 
    def countComponents(self, n: int, edges: List[List[int]]) -> int: 
        res = 0 
        adj = defaultdict(list) 
        for u, v in edges: 
            # undirected graph = 2 ways 
            adj[u].append(v) 
            adj[v].append(u) 
        visited = set() 

        def dfs(node): 
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
                dfs(i) 
                res += 1 
        return res