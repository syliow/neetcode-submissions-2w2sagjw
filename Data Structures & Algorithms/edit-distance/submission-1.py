class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}
        m, n = len(word1), len(word2)

        def dfs(i, j):
            # base case
            if i == m:
                return n - j

            # base case: out of options
            if j == n:
                return m - i

            # memo check
            if (i, j) in dp:
                return dp[(i, j)]

            # recursion
            # MIN num of operations
            # insert , del , replace
            res = 0
            # if both side matches:
            if word1[i] == word2[j]:
                res = dfs(i + 1, j + 1)
            else:
                res = min(1 + dfs(i + 1, j), 1 + dfs(i + 1, j + 1), 1 + dfs(i, j + 1))

            dp[(i, j)] = res
            return res

        return dfs(0, 0)
