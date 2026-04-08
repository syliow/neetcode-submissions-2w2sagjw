class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum == target:
                return [l+ 1, r + 1]
            #if sum > target, means we need smaller num, r--
            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
        
        return []