class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #core idea: insert num into every possible slot
        if len(nums) == 0:
            return [[]]
        #insert the digit at index 1 to every possible index
        perms = self.permute(nums[1:])
        res = []
        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)
        return res