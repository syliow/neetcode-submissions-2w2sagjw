class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        adj = defaultdict(list)

        for prereq, course in prerequisites:
            adj[prereq].append(course)

        # memo cache (to resolve TLE)
        memo = {}

        # check if u can reach v
        def dfs(crs, target):
            # memo check
            if (crs, target) in memo:
                return memo[(crs, target)]

            # base case: u leads to target
            if target in adj[crs]:
                memo[(crs, target)] = True
                return True

            # queries [u, j] check if u is pre-req of j
            for nei in adj[crs]:
                if dfs(nei, target):
                    memo[(nei, target)] = True
                    return True
            # fallback
            memo[(crs, target)] = False
            return False

        # go through all course
        res = []
        for u, v in queries:
            res.append(dfs(u, v))
        return res
