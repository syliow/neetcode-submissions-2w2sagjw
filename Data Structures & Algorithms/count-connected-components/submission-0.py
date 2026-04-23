class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visit = set()
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node):
            #mark the current node as visited
            visit.add(node)
            for nei in adj[node]:
                if nei not in visit:
                    dfs(nei)
            
        res = 0
        #go thru every possible node
        for node in range(n):
            #if nvr see this node, its a new component
            if node not in visit:
                dfs(node)
                res += 1
        return res
            
