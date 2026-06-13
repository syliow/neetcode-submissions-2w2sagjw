class Solution:
    def encode(self, strs: List[str]) -> str:
        # we can use strLength#strs to encode it
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res

    def decode(self, s: str) -> List[str]:
        # we can split the substrings using split()
        # use the strLength to jump to str
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])  # length could be double digit so cant use i - 1
            i = j + 1  # word starts after #, end after length charas
            j = i + length
            res.append(s[i:j])
            i = j  # skip pointer to next prefix
        return res
