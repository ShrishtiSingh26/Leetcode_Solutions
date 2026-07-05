# Last updated: 7/5/2026, 7:41:40 PM
class Solution(object):
    def repeatedNTimes(self, nums):
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            if freq[num] > 1:
                return num
