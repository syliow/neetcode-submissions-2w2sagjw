class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        # enumerate is important to get both index and value
        for i, n in enumerate(nums):
            diff = target - n
            
            #if num is already in map, then it means we found the 2sum
            if diff in prevMap:
                return [prevMap[diff], i]
            
            #if num not in map, add it since we went thru it
            prevMap[n] = i