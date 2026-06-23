class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # non decreasing order, find target = Binary search
        ROWS, COLS = len(matrix), len(matrix[0])
        # two pass
        # first pass, find which row it is at
        # second pass, find target
        top, btm = 0, ROWS - 1
        while top < btm:
            mid = (top + btm) // 2
            if target < matrix[mid][0]:
                btm = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                top = mid
                break  
        # make sure we dun go out of range
        if not top <= btm:
            return False

        # 2nd pass
        l, r = 0, COLS - 1
        while l <= r:
            mid = (l + r) // 2
            if target == matrix[top][mid]:
                return True
            elif target < matrix[top][mid]:  # smaller, look Left
                r = mid - 1
            elif target > matrix[top][mid]:  # bigger, look right
                l = mid + 1
        # fallback
        return False
