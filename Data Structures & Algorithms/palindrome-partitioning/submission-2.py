class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # pattern: return all possible substr -> backtracking : return list
        # backtracking -> DFS
        res = []
        pair = []

        #check for palindrome
        def isPalindrome(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                #expand outwards
                l += 1
                r -= 1
            return True

        def dfs(i):
            # base case
            if i >= len(s):
                res.append(pair.copy())
                return
            #backtracking
            for j in range(i, len(s)):
                if isPalindrome(s, i, j):
                    pair.append(s[i: j + 1]) #choose
                    dfs(j + 1) #explore
                    pair.pop() #unchoose
                    

        dfs(0)
        return res