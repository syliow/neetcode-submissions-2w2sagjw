class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}

        def dfs(i):
            if i == len(s):
                return True
            #memo check
            if i in dp:
                return dp[i]
            for word in wordDict:
                if i + len(word) <= len(s) and s[i: i + len(word)] == word:
                    if dfs(i + len(word)):
                        dp[i] = True
                        return True
            dp[i] = False
            return False
        return dfs(0)