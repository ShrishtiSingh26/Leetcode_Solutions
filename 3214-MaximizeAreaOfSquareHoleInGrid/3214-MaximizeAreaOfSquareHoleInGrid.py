# Last updated: 7/5/2026, 7:40:08 PM
class Solution(object):
    def maximizeSquareHoleArea(self, n, m, hBars, vBars):
        def max_consecutive_gap(bars):
            if not bars:
                return 1
            
            bars.sort()
            max_len = 1
            curr = 1
            
            for i in range(1, len(bars)):
                if bars[i] == bars[i - 1] + 1:
                    curr += 1
                else:
                    curr = 1
                max_len = max(max_len, curr)
            
            return max_len + 1
        
        max_h = max_consecutive_gap(hBars)
        max_v = max_consecutive_gap(vBars)
        
        side = min(max_h, max_v)
        return side * side