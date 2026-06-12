class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # pattern: DFS
        adj = defaultdict(list)
        for a, b in prerequisites:
            adj[a].append(b)
        visited = set()
        visiting = set()
        res = []

        def dfs(crs):
            if crs in visited:
                return True
            if crs in visiting:
                return False  # cycle = invalid
            visiting.add(crs)

            # explore neighbors
            for nei in adj[crs]:
                if not dfs(nei):
                    return False
            # check all neighbors before we update
            visiting.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True

        # run for all courses
        for i in range(numCourses):
            if not dfs(i):
                return []  # in case we cannot finish course
        return res
