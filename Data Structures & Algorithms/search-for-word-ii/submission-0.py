class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

    def addWord(self, word):
        cur = self
        # loop thru chara one by one
        for c in word:
            if c not in cur.children:
                # add it
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # core idea: dfs + backtracking recursion
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res = []
        visited, res = set(), set()

        def dfs(r, c, node, word):
            # base case
            if (
                r < 0
                or c < 0
                or r >= ROWS
                or c >= COLS
                or (r, c) in visited
                or board[r][c] not in node.children
            ):
                return

            # backtrack (include, recursion, exclude)
            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.endOfWord:
                res.add(word)

            # dfs 4 directions
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            visited.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)
