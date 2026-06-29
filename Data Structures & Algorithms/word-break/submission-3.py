class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # pattern: top down memoization
        dp = {}

        def dfs(i):
            # base case
            if i == len(s):
                return True
            # memo check
            if i in dp:
                return dp[i]
            # recursion
            for word in wordDict:
                if (i + len(word)) <= len(s) and s[i : i + len(word)] == word:
                    if dfs(i + len(word)):
                        dp[i] = True
                        return True
            # fallback
            dp[i] = False
            return False

        return dfs(0)