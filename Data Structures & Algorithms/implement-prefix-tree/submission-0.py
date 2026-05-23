class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        #start from root
        cur = self.root

        #loop through each chara 1 by 1
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode() #if doesnt exists, we add it
            cur = cur.children[c]
        #mark as last chara
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord #check is it end of word
        
    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True #dunnid to check last chara
        