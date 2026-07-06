class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # pattern: graph, adj list
        # we dunnid to know who trusted who, count is enuf
        incoming = defaultdict(int)
        outgoing = defaultdict(int)

        # a: people, b: people who trusted b
        for a, b in trust:
            outgoing[a] += 1
            incoming[b] += 1

        # judge criteria:
        # not appear in a
        # should be in every b
        # only 1 ppl is judge
        for i in range(1, n + 1):
            if outgoing[i] == 0 and incoming[i] == n - 1:
                return i
        # fallback
        return -1
