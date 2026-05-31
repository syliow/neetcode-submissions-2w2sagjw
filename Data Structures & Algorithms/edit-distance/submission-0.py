class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # pattern: recursion
        dp = {}  # (i, j) : operationCount
        # subproblem: do we insert? do we delete? do we replace?

        def dfs(i, j):
            res = 0
            # base case
            # word2 matches, check word1
            if j == len(word2):
                return len(word1) - i

            # out of bounds for word1, check word2
            if i >= len(word1):
                return len(word2) - j

            # check memo
            if (i, j) in dp:
                return dp[(i, j)]

            # recursion
            # we only move j forward if i == j
            # insert, del , replace
            if word1[i] == word2[j]:
                res += dfs(i + 1, j + 1)
            # otherwise we should find out which operation
            else:
                res += min(1 + dfs(i + 1, j), 1 + dfs(i + 1, j + 1), 1 + dfs(i, j + 1))
            dp[(i, j)] = res
            return res

        return dfs(0, 0)
