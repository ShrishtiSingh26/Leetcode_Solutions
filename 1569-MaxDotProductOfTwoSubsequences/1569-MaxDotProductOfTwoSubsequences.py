# Last updated: 7/5/2026, 7:41:12 PM
class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        n, m = len(nums1), len(nums2)
        
        # Initialize DP with very small values
        dp = [[float('-inf')] * (m + 1) for _ in range(n + 1)]
        
        for i in range(n):
            for j in range(m):
                product = nums1[i] * nums2[j]
                
                dp[i+1][j+1] = max(
                    product,                  # start new subsequence
                    dp[i][j] + product,       # extend previous subsequence
                    dp[i][j+1],               # skip nums1[i]
                    dp[i+1][j]                # skip nums2[j]
                )
        
        return dp[n][m]