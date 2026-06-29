class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # pattern: btm up approach
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True  # base case

        # start from backwards, R -> L
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                # since current word matches
                # i index success depends on the word after
                if s[i : i + len(word)] == word and dp[i + len(word)]:
                    dp[i] = True
                    break
        return dp[0]
