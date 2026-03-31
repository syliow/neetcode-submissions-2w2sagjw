class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            
            #Otherwise if not seen before, add it to seen
            seen.add(num)
        return False
        