# Last updated: 7/5/2026, 7:40:00 PM
import heapq

class Solution(object):
    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        two_smallest = heapq.nsmallest(2, nums[1:])
        return nums[0] + two_smallest[0] + two_smallest[1]

