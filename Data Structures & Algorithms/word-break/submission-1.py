class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # pattern: btm up approach (R -> L)
        n = len(s)
        dp = [False] * (n + 1)

        # base case
        dp[n] = True  # last index is always true
        # start from last
        for i in range(n - 1, -1, -1):
            # its basically just comparing chara at index vs worddict
            # eg: e, de, ode, code vs "neet", "code"
            for w in wordDict:
                # if substring matches word, and the remaining must also match
                if s[i : i + len(w)] == w and dp[i + len(w)]:
                    dp[i] = True
                    break

        return dp[0]
