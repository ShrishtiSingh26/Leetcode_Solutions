# Last updated: 7/5/2026, 7:40:24 PM
class Solution:
  def separateDigits(self, nums: list[int]) -> list[int]:
    return [int(c) for num in nums for c in str(num)]