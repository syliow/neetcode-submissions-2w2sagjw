class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # 1. Ensure every unique letter exists as a graph node
        adj = {}
        for w in words:
            for c in w:
                adj[c] = set()

        # 2. Derive letter order by finding dependencies between words
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))

            # Catch invalid sorting where a shorter prefix follows a longer word
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            # Only the first differing character establishes a relative order
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        # 3. Track state to detect cycles and build sequence
        visited = {}  # True = on current path (cycle), False = fully processed
        res = []

        def dfs(char):
            # If already visited, return True to signal a cycle
            if char in visited:
                return visited[char]

            visited[char] = True  # Backtracking protection: mark as active on path

            for neighChar in adj[char]:
                if dfs(neighChar):
                    return True

            visited[char] = False  # Safe to reuse: no cycles found from here
            res.append(char)  # Leaf nodes must appear last in alphabet

        # 4. Process all independent components of the alphabet
        for char in adj:
            if dfs(char):
                return ""

        # 5. Reverse because deep dependencies were collected first
        res.reverse()
        return "".join(res)
