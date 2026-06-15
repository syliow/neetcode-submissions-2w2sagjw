class TrieNode:
    def __init__(self):
        self.children = {}  # a: TrieNode
        self.endOfWord = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root  # start from root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            # if c in chidlren
            cur = cur.children[c]
        cur.endOfWord = True  # mark as last chara

    def search(self, word: str) -> bool:
        # dfs recursion
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":  # . is FFA chara
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True  # if found any chara matches FFA, true
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.endOfWord

        return dfs(0, self.root)
