class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #no dup = sort, skip
        res = []
        nums.sort()

        def backtrack(i, subset):
            #out of bounds
            if i == len(nums):
                res.append(subset.copy())
                return
            
            #include num
            subset.append(nums[i])
            backtrack(i + 1, subset)
            #exclude num
            subset.pop()
            
            #skip over dup
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i +=1 #move to next num
            backtrack(i + 1, subset)
        
        backtrack(0, [])
        return res