# Last updated: 7/5/2026, 7:41:28 PM
class Solution(object):
    def maxSideLength(self, mat, threshold):
        m, n = len(mat), len(mat[0])
        
        # prefix sum
        pre = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                pre[i + 1][j + 1] = (
                    mat[i][j]
                    + pre[i][j + 1]
                    + pre[i + 1][j]
                    - pre[i][j]
                )
        
        def exists(k):
            for i in range(k, m + 1):
                for j in range(k, n + 1):
                    total = (
                        pre[i][j]
                        - pre[i - k][j]
                        - pre[i][j - k]
                        + pre[i - k][j - k]
                    )
                    if total <= threshold:
                        return True
            return False
        
        lo, hi, ans = 0, min(m, n), 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if exists(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        
        return ans
