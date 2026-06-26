class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()

        for t in triplets:
            # filter out any pairs of triplets that contain value > target[i]
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i, v in enumerate(t):
                # as long any pair triplet contains index that == target[i]
                # add 1 to good
                if v == target[i]:
                    good.add(i)

        return len(good) == 3
