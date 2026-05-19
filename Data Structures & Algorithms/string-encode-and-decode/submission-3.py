class Solution:
    def encode(self, strs: List[str]) -> str:
        # early return
        if len(strs) == 0:
            return ""
        arr = ""
        # idea: add a length and # -> length#oristr
        for s in strs:
            length = str(len(s))
            arr += length + "#" + s
        return arr

    def decode(self, s: str) -> List[str]:
        # early return
        if len(s) == 0:
            return []
        # L  pointer
        i = 0
        res = []

        while i < len(s):
            j = i

            while s[j] != "#":  # get the length
                j += 1  # i will stop when it reaches #, j will start at str

            length = int(s[i:j])  # stop before j
            # j starts at str, j until end of s
            start = j + 1
            word = s[start : start + length]
            res.append(word)

            # i move to next word
            i = start + length
        return res
