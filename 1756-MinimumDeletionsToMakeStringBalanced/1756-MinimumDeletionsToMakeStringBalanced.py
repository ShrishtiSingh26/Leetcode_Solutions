# Last updated: 7/5/2026, 7:41:02 PM
class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        deletions = 0
        count_b = 0
        
        for ch in s:
            if ch == 'b':
                count_b += 1
            else:  # ch == 'a'
                deletions = min(deletions + 1, count_b)
        
        return deletions