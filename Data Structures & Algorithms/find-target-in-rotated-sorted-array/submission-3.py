class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            elif nums[mid] < nums[r]:
                # search R
                # mid < target <= R
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

            else:
                # search L
                # L <= target < mid
                if nums[l] <= target < nums[mid]:
                    r = mid - 1  # search L
                else:
                    l = mid + 1

        # fallback
        return -1
