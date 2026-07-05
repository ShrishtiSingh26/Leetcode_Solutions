# Last updated: 7/5/2026, 7:39:45 PM
from typing import List

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        
        for i in range(n):
            idx = (i + nums[i]) % n
            res[i] = nums[idx]
        
        return res

