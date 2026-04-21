class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #Rot oren = virs , spread to adjacent 4 direction
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        time = 0
        
        directions = [
            [0, 1], [0, -1], [1, 0], [-1, 0]
        ]
        #to count how many fresh orange we have initally 
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh +=1
                if grid[r][c] == 2:
                    q.append((r, c))
        
        while fresh > 0 and q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    #check for base case
                    if (row in range(ROWS) and 
                        col in range(COLS) and
                        grid[row][col] == 1):
                            grid[row][col] = 2 #mark as rot
                            q.append((row, col)) #add new rot to q
                            fresh -= 1
            time += 1
        return time if fresh == 0 else -1 