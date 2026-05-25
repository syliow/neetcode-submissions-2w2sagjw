class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #Hierholzer's algorithm
        #idea: build path backwards with backtracking
        #include, backtrack, exclude
        adj = defaultdict(list)
        res = [] #store the whole schedule
        #sort the name 
        for src, dst in sorted(tickets)[::-1]:
            #[src: [multiple destinations]]
            adj[src].append(dst) 
        
        def dfs(src):
            while adj[src]:
                dst = adj[src].pop()
                #continue check
                dfs(dst)
            res.append(src) #after pop, add to res for schedule
        
        #initial start is jfk
        dfs("JFK")
        #sort the whole list (dsc alphabet order)
        return res[::-1]
        