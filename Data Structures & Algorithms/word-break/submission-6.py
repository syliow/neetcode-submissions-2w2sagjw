class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}

        def dfs(i):
            # base case
            if i == len(s):
                return True

            # memo check
            if i in dp:
                return dp[i]

            # recursion
            res = False
            for word in wordDict:
                # after slice it direct match the word
                if s[i : i + len(word)] == word:
                    # continue loop
                    if dfs(i + len(word)):
                        res = True
            # fallback
            dp[i] = res
            return res

        return dfs(0)
