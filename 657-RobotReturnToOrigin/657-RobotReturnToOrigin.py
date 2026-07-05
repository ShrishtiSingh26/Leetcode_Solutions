# Last updated: 7/5/2026, 7:41:57 PM
class Solution:
  def judgeCircle(self, moves: str) -> bool:
    return moves.count('R') == moves.count('L') and moves.count('U') == moves.count('D')