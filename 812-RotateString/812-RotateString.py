# Last updated: 7/5/2026, 7:41:47 PM
class Solution:
  def rotateString(self, s: str, goal: str) -> bool:
    return len(s) == len(goal) and goal in s + s