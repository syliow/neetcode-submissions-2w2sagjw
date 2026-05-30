class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #start with creating btm row fill with 1s
        btmRow = [1] * n

        #move the row upward, creating one top row at a time
        for i in range(m-1):
            topRow = [1] * n

            #scan from R -> L
            #start from n-2 is bcs n-1 (last col is always 1)
            #bcs we can only go down
            for j in range(n-2, -1, -1):
                #res = right + down
                topRow[j] = topRow[j + 1] + btmRow[j]
            
            #current topRow -> btmRow for next lvl
            btmRow = topRow
        #start from top left
        return btmRow[0]