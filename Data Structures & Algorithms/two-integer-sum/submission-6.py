class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for i, v in enumerate(nums):
            if target - v in numMap:
                return [numMap[target - v], i]
            numMap[v] = i
