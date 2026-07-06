class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        res = 0  # num of boats (min)
        # core idea: max is 2 ppl
        # pair heaviest with lightest
        # if can share, good. otherwise heavy ppl = 1 boat
        while l <= r:
            remain = limit - people[r]
            r -= 1
            res += 1

            if l <= r and remain >= people[l]:
                l += 1
        return res
