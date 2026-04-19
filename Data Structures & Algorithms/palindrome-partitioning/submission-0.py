class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    part.append(s[i : j + 1]) #add substr to part
                    #backtracking
                    dfs(j + 1)
                    part.pop()
            
        dfs(0)
        return res

    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l = l + 1
            r = r - 1
        return True