class Solution:
    def numDecodings(self, s: str) -> int:
        # pattern: btm up approach (r -> L) (SPACE OPTIMIZED)
        # subproblem: how many ways can i decode a msg at index i?
        # <----- R- L

        n = len(s)
        # <---- cur prev1 prev2
        prev1, prev2 = 1, 1 #single chara count as 1 way

        for i in reversed(range(n)):
            # make sure first digit doesnt start with 0
            # it should only start with either 1 / 2
            # and 2nd digit should be in "123456" for 20s
            if s[i] == "0":
                cur = 0
            else:
                # decode single digit
                cur = prev1

            # case 2: decode double digit
            if i + 1 < n and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                cur += prev2

            # move pointer forward
            prev1, prev2 = cur, prev1

        return prev1
