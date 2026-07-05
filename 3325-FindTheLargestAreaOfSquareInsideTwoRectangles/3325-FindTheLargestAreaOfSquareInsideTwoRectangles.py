# Last updated: 7/5/2026, 7:39:59 PM
class Solution(object):
    def largestSquareArea(self, bottomLeft, topRight):
        """
        :type bottomLeft: List[List[int]]
        :type topRight: List[List[int]]
        :rtype: int
        """
        n = len(bottomLeft)
        max_area = 0

        for i in range(n):
            for j in range(i + 1, n):
                # Overlapping rectangle coordinates
                x_left = max(bottomLeft[i][0], bottomLeft[j][0])
                y_bottom = max(bottomLeft[i][1], bottomLeft[j][1])
                x_right = min(topRight[i][0], topRight[j][0])
                y_top = min(topRight[i][1], topRight[j][1])

                # Check if overlap exists
                if x_right > x_left and y_top > y_bottom:
                    side = min(x_right - x_left, y_top - y_bottom)
                    max_area = max(max_area, side * side)

        return max_area
