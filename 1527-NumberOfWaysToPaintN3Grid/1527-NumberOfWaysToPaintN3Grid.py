# Last updated: 7/5/2026, 7:41:14 PM
class Solution(object):
    def numOfWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        same = 6  # ABA patterns
        diff = 6  # ABC patterns
        
        for _ in range(1, n):
            new_same = (same * 3 + diff * 2) % MOD
            new_diff = (same * 2 + diff * 2) % MOD
            same, diff = new_same, new_diff
        
        return (same + diff) % MOD
