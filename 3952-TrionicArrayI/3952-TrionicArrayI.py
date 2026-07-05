# Last updated: 7/5/2026, 7:39:24 PM
class Solution(object):
    def isTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n < 4:   # need at least 1 element per phase
            return False
        
        i = 0
        
        # phase 1: strictly increasing
        start = i
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
        if i == start:
            return False
        
        # phase 2: strictly decreasing
        start = i
        while i + 1 < n and nums[i] > nums[i + 1]:
            i += 1
        if i == start:
            return False
        
        # phase 3: strictly increasing
        start = i
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
        if i == start:
            return False
        
        # must consume entire array
        return i == n - 1
