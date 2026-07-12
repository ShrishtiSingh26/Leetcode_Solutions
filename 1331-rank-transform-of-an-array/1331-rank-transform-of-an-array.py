from typing import List
from bisect import bisect_right

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Create a sorted list of unique elements from the array
        # This represents all distinct values in ascending order
        unique_sorted = sorted(set(arr))
      
        # For each element in the original array, find its rank
        # bisect_right returns the insertion position, which equals the rank
        # since we're using 1-based ranking (position 0 means rank 1)
        return [bisect_right(unique_sorted, x) for x in arr]