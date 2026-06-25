from collections import defaultdict, deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Edge case check
        if endWord not in wordList:
            return 0

        # --- PATTERN 1: BUILD GRAPH (Adjacency List) ---
        nei = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                # Wildcard pattern (e.g., "h*t")
                pattern = word[:j] + "*" + word[j + 1 :]
                nei[pattern].append(word)

        # --- PATTERN 2: BFS INITIALIZATION ---
        visited = set([beginWord])
        q = deque([beginWord])
        res = 1  # Tracks path level

        # --- PATTERN 3: LAYER-BY-LAYER BFS TRAVERSAL ---
        while q:
            # Snapshot of current level size
            for _ in range(len(q)):
                word = q.popleft() 

                # Target found
                if word == endWord:
                    return res

                # Expand current node's neighbors
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1 :]
                    for neiWord in nei[pattern]:
                        # Prevent processing duplicates
                        if neiWord not in visited:
                            visited.add(neiWord)
                            q.append(neiWord)  # Queue next level
            res += 1  # Move to next layer

        return 0  # Target unreachable
