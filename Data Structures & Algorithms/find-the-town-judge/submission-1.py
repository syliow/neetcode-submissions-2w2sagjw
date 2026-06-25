class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # [[1,3],[4,3],[2,3]]
        # 1 trust 3
        # 4 trust 3
        # 2 trust 3
        # 3 trust nobody, everyone trust 3
        # [[1,3],[2,3],[3,1],[3,2]]
        # 1 trust 3
        # 2 trust 3
        # 3 trust 1
        # 3 trust 2
        # everyone trust diff so -1
        # pattern graph, adj list
        trusts = defaultdict(list)
        trustedBy = defaultdict(list)
        for a, b in trust:
            trusts[a].append(b)
            trustedBy[b].append(a)
        # judge is somewho who trusts no one and trusted by everyone
        for person in range(1, n + 1):
            if len(trusts[person]) == 0 and len(trustedBy[person]) == n - 1:
                return person
        # fallback
        return -1
