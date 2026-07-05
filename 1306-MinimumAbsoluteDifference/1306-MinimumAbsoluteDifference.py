# Last updated: 7/5/2026, 7:41:33 PM
class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        n = len(arr)
        
        min_diff = float('inf')
        for i in range(n - 1):
            min_diff = min(min_diff, arr[i + 1] - arr[i])
        
        res = []
        for i in range(n - 1):
            if arr[i + 1] - arr[i] == min_diff:
                res.append([arr[i], arr[i + 1]])
        
        return res
