# Last updated: 7/5/2026, 7:40:43 PM
class Solution:
  def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
    for _ in range(4):
      if mat == target:
        return True
      mat = [list(x) for x in zip(*mat[::-1])]
    return False