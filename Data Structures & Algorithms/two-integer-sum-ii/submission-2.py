class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # o1 space, cannot use arr or set
        # pattern: LR pointer (sorted in non decreasing order <- big hint)
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]  # return index but 1-indexed
            elif numbers[l] + numbers[r] < target:  # need larger num
                l += 1
            else:
                r -= 1
