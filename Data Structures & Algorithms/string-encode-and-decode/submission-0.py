class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            #count the length of string and add a "#"
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        #main idea:4#neet , stops before #, extract how many length to cut
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            #convert the chara before # into int (length)
            length = int(s[i:j])
            #move the pointer one after #
            i = j + 1
            j = i + length
            #slice the str from i -> j and add it to res
            res.append(s[i:j])
            i = j

        return res
