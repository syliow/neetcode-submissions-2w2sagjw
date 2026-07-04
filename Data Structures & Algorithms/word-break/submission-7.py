class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {len(s): True}

        def dfs(i):
            # base case
            if i == len(s):
                return True

            # memo check
            if i in dp:
                return dp[i]

            # recursion
            for word in wordDict:
                # after slice it direct match the word
                if s[i : i + len(word)] == word:
                    # continue loop
                    if dfs(i + len(word)):
                        dp[i] = True
                        return True
            # fallback
            dp[i] = False
            return False

        return dfs(0)
