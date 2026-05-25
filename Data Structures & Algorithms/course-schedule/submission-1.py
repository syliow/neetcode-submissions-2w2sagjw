class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # pattern: dfs, we want to go deep
        visiting = set()
        visited = set()
        # map to look up course: prereq
        crsMap = {i: [] for i in range(numCourses)}
        for crs, prereq in prerequisites:
            crsMap[crs].append(prereq)

        # know which course we are looking
        def dfs(course):
            # base case
            if course in visited:
                return True
            # if cours already in path = false
            if course in visiting:
                return False

            # only proceed with check if we havent check before
            visiting.add(course)
            # loop thru course prereq
            for pre in crsMap[course]:
                if not dfs(pre):  # keep on finding course pre req
                    return False
            visiting.remove(course)
            visited.add(course)
            return True

        # loop thru each course
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
