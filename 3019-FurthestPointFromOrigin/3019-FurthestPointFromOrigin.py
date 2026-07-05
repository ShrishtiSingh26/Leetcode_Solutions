# Last updated: 7/5/2026, 7:40:10 PM
class Solution:
  def furthestDistanceFromOrigin(self, moves: str) -> int:
    return abs(moves.count('L') - moves.count('R')) + moves.count('_')