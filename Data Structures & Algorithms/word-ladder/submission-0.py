class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Endword must be in wordlist
        if endWord not in wordList:
            return 0
        
        nei = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                nei[pattern].append(word)
        
        visited = set([beginWord])
        q = deque([beginWord])
        res = 1 # Min length is 1

        while q:
            for i in range(len(q)):
                word = q.popleft() # Fixed indentation
                
                # From start reach to last word
                if word == endWord:
                    return res
                    
                # Otherwise continue bfs
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visited:
                            visited.add(neiWord) # Fixed typo: changed 'visit' to 'visited'
                            q.append(neiWord)
            res += 1
        return 0