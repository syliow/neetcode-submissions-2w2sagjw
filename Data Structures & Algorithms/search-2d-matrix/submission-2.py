class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # pattern: sorted in non decreasing
        # find a num within sorted arr

        ROWS, COLS = len(matrix), len(matrix[0])
        # idea: 2 pass, one find the row num at
        # bs in the selected row

        # First pass
        top, btm = 0, ROWS - 1
        while top <= btm:
            row = (top + btm) // 2

            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:  # need go smaller
                btm = row - 1
            else:
                break
        if not top <= btm:
            return False

        # Second pass
        row = (top + btm) // 2
        l, r = 0, COLS - 1

        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False #fallback
