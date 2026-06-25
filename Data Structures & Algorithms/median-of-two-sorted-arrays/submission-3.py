class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        # Slicing the merged array perfectly in half (left-leaning for odd totals)
        half = (total + 1) // 2

        # Ensure A is always the shorter array so binary search range is minimal
        if len(B) < len(A):
            A, B = B, A

        # l and r now represent the NUMBER of elements we take from A
        l, r = 0, len(A)

        while l <= r:
            i = (l + r) // 2   # Count of elements taken from A
            j = half - i       # Count of elements taken from B (no more "- 2"!)

            # Fetch boundary values using slice counts (index is count - 1)
            Aleft  = A[i - 1] if i > 0 else float("-inf")
            Aright = A[i]     if i < len(A) else float("inf")

            Bleft  = B[j - 1] if j > 0 else float("-inf")
            Bright = B[j]     if j < len(B) else float("inf")

            # Check if partition is perfectly balanced
            if Aleft <= Bright and Bleft <= Aright:
                # ODD total: The median is simply the largest element on the left side
                if total % 2 != 0:
                    return float(max(Aleft, Bleft))
                
                # EVEN total: Average of the maximum left element and minimum right element
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0

            # Adjust Binary Search range
            elif Aleft > Bright:
                r = i - 1  # We took too many elements from A, move left
            else:
                l = i + 1  # We took too few elements from A, move right