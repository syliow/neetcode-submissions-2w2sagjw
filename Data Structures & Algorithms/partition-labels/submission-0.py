class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        # first pass: build map for chara count
        for i, c in enumerate(s):
            lastIndex[c] = i

        # second pass: extend the chara index
        res = []
        size = end = 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])

            if i == end:
                res.append(size)
                size = 0  # reset size for every chara
        return res
