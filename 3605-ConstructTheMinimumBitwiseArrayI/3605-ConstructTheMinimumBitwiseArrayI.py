# Last updated: 7/5/2026, 7:39:47 PM
class Solution(object):
    def minBitwiseArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []

        for x in nums:
            if x % 2 == 0:
                res.append(-1)
                continue

            k = 0
            temp = x
            while temp & 1:
                k += 1
                temp >>= 1

            res.append(x - (1 << (k - 1)))

        return res
