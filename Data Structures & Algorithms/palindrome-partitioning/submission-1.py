class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #i = index
        #every backtrack -> slice s[i] 
        #sliced i will be decided to add or pop from pair
        res, pair = [], []

        def dfs(i):
            #base case
            if i >= len(s):
                res.append(pair.copy())
                return
            
            #core idea: add -> recursion -> pop
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    pair.append(s[i: j + 1])
                    dfs(j + 1)
                    pair.pop()
        dfs(0)
        return res
        
    
    def isPali(self, s, l, r):
            while l < r:
                # palindrome check
                if s[l] != s[r]:
                    return False
                # move pointers forward/backward
                l, r = l + 1, r - 1
            return True
    