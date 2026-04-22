class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj[crs].append(pre)

        res = []
        cycle = set()
        seen = set()

        def dfs(crs):
            if crs in cycle: return False
            if crs in seen: return True

            cycle.add(crs)
            for pre in adj[crs]:
                if not dfs(pre): return False
            
            cycle.remove(crs)
            seen.add(crs)

            res.append(crs)
            return True

        for c in range(numCourses):
            if not dfs(c): return [] #return empty list if invalid
        
        return res