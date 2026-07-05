# Last updated: 7/5/2026, 7:39:46 PM
class Solution(object):
    def minBitwiseArray(self, nums):
        res = []
        for b in nums:
            if b % 2 == 0:
                res.append(-1)
                continue

            k = 0
            while (b >> k) & 1:
                k += 1

            res.append(b - (1 << k) + (1 << (k - 1)))
        return res
