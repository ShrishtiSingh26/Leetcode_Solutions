# Last updated: 7/5/2026, 7:41:52 PM
import bisect

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        i = bisect.bisect_right(letters, target)
        return letters[i % len(letters)]
