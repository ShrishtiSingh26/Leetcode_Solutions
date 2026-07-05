# Last updated: 7/5/2026, 7:40:39 PM
class Solution(object):
    def maxMatrixSum(self, matrix):
        total = 0
        neg_count = 0
        min_abs = float('inf')
        
        for row in matrix:
            for val in row:
                if val < 0:
                    neg_count += 1
                abs_val = abs(val)
                total += abs_val
                min_abs = min(min_abs, abs_val)
        
        if neg_count % 2 == 1:
            total -= 2 * min_abs
        
        return total
