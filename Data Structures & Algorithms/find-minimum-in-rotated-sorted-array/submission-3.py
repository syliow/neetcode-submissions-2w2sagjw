class Solution:
    def findMin(self, nums: List[int]) -> int:
        #pattern: sorted in asc order, log n time
        #core idea: find out which side is sorted first
        l, r = 0, len(nums) - 1
        
        #we dun wan LR point at same index
        while l < r:
            mid = (l + r) // 2
            #[1, 2, 3(mid), 4, 5, 6], mid < r: sorted on Left
            if  nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        #either L or R is fine bcs it will stop at one 
        return nums[l]

