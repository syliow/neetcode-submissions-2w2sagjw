class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        visited = set()
        for u, v in prerequisites:
            adj[v].append(u)

        def dfs(crs):
            # base case
            if crs in visited:
                return False
            visited.add(crs)

            for nei in adj[crs]:
                if not dfs(nei):
                    return False
            visited.remove(crs)
            return True  # Fallback after looking thru all nei

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
