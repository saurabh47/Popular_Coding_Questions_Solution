### Problem 223. Rectangle Area (Medium): https://leetcode.com/problems/rectangle-area/
### Tags: Math, Geometry
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        a1 = (ax2-ax1) * (ay2-ay1)
        a2 = (bx2-bx1) * (by2-by1)

        # no overlapping
        if((ax2 < bx1 or ax1 > bx2) or ((by2 <= ay1) or (by1 >= ay2))):
            return a1 + a2
        x1 = max(ax1, bx1)
        y1 = max(ay1, by1)

        x2 = min(ax2, bx2)
        y2 = min(ay2, by2)

        overlapped = abs(x2-x1) * abs(y2-y1)

        return a1 + a2 - overlapped