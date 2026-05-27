class Solution:
    def numDecodings(self, s: str) -> int:
        # Indices:      ...    i        i+1          i+2
        # Variables:          [🎯]     [⏩]         [⏭️]
        #                    current    one          two
        # 🏁 1. Base cases at the very end of the string
        one = 1  # 1 step ahead (empty string = 1 valid path)
        two = 0  # 2 steps ahead (out of bounds = 0 ways)

        # btm up approach: start at last, stop by 0 , decrement pos by -1
        for i in range(len(s) - 1, -1, -1):
            # 0 cannot be the starting digit
            if s[i] == "0":
                cur = 0
            else:
                cur = one  # Single-digit combo takes the 'one' step ways

            # inside bounds and val = 10 - 26
            if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                cur += two

            # move pointer backwards for next iteration
            two = one
            one = cur

        # return total way at front
        return one
