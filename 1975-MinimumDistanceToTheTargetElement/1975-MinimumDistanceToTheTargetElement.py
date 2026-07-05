# Last updated: 7/5/2026, 7:40:48 PM
class Solution:
  def getMinDistance(self, nums: list[int], target: int, start: int) -> int:
    ans = math.inf

    for i, num in enumerate(nums):
      if num == target:
        ans = min(ans, abs(i - start))

    return ans