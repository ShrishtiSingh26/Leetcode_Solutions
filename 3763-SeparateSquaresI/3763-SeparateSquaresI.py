# Last updated: 7/5/2026, 7:39:41 PM
class Solution(object):
    def separateSquares(self, squares):
        total = 0.0
        for _, _, l in squares:
            total += l * l
        half = total / 2.0

        low, high = 0.0, 0.0
        for _, y, l in squares:
            high = max(high, y + l)

        def area_below(y_line):
            area = 0.0
            for _, y, l in squares:
                if y < y_line:
                    area += l * min(y_line - y, l)
            return area

        eps = 1e-5
        while high - low > eps:
            mid = (low + high) / 2.0
            if area_below(mid) >= half:
                high = mid
            else:
                low = mid

        return high
