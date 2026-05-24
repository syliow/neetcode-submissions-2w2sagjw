class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        #up down left right
        directions = [
            [0, 1], [1, 0], [-1, 0], [0, -1]
        ]
        res = 0 #island count

        def dfs(r, c):
            #base case: invalid case
            if (
                r < 0 or c < 0 or r >= ROWS or c >= COLS or
                (r, c) in visited or grid[r][c] == "0"
            ):
                return False
            
            #recursion idea: include backtrack exclude
            #note: need to mark island as visited to avoid dup
            visited.add((r, c))
            grid[r][c] = "0"

            #go thru 4 directions
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            #note: no need remove from set bcs visited = history
            #just update island to 0 to avoid revisit
            # visited.remove((r, c))
            return True
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c): #if invalid case return false
                    res += 1
        return res