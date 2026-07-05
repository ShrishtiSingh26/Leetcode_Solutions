# Last updated: 7/5/2026, 7:41:23 PM
class Solution:
  def sortByBits(self, arr: list[int]) -> list[int]:
    return sorted(arr, key=lambda x: (x.bit_count(), x))