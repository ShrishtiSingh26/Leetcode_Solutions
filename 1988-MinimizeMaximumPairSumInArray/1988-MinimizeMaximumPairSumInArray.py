# Last updated: 7/5/2026, 7:40:46 PM
class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        ans = 0

        for i in range(n // 2):
            ans = max(ans, nums[i] + nums[n - 1 - i])

        return ans
