class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visiting = set()
        visited = set()

        crsMap = {i: [] for i in range(numCourses)}
        for crs, prereq in prerequisites:
            crsMap[crs].append(prereq)

        res = []

        def dfs(course):
            # base case:
            if course in visited:
                return True

            if course in visiting:
                return []  # cycle detected
            # add , dfs, remove
            visiting.add(course)
            for pre in crsMap[course]:
                if not dfs(pre):
                    return []  # cycle detected
            visiting.remove(course)
            visited.add(course)
            res.append(course)
            return True

        # loop thru each course
        for c in range(numCourses):
            if not dfs(c):
                return []  # cycle detected
        return res if res else []
