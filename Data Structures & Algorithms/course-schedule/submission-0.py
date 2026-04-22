class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj[crs].append(pre)

        cycle = set() #nodes in current path
        seen = set() #nodes fully processed

        def dfs(crs):
            if crs in cycle: return False
            if crs in seen: return True

            cycle.add(crs)
            for pre in adj[crs]: #go thru each req
                if not dfs(pre): return False
            
            cycle.remove(crs)
            seen.add(crs)
            return True

        #2. check every course (in case not linked)
        for c in range(numCourses):
            if not dfs(c): return False
        
        return True