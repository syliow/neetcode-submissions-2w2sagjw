class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # hint: non decreasing order
        # o(1) space = set or map
        # pattern: L R pointer
        # idea: L + R = target?
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            elif numbers[l] + numbers[r] < target:
                # need larger num
                l += 1
            else:
                # need smaller num
                r -= 1
