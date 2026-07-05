# Last updated: 7/5/2026, 7:39:04 PM
class Solution:
    def mirrorDistance(self, n: int) -> int:
        return abs(n - int(str(n)[::-1]))