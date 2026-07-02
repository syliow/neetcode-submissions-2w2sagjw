class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for prereq, crs in prerequisites:
            adj[crs].append(prereq)
        
        prereqMap = {}

        def dfs(crs):
            if crs in prereqMap:
                return prereqMap[crs]
            
            #empty set for this course
            prereqMap[crs] = set()
            #continue update course link in map through deep dfs
            for prereq in adj[crs]:
                prereqMap[crs].update(dfs(prereq))
            
            #add crs itself in initial link
            prereqMap[crs].add(crs)
            return prereqMap[crs]

        for crs in range(numCourses):
            dfs(crs)
        
        res = []
        for u, v in queries:
            res.append(u in prereqMap[v])
        return res