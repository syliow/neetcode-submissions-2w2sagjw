class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1, prev2 = 0, 0

        for money in nums:
            # determine max money for the cur house
            # either we rob cur or skip cur
            # we can only run current, if our last rob is 2 house ago
            current = max(money + prev2, prev1)

            # slide window forward until end
            prev2 = prev1
            prev1 = current

        return prev1
