# Last updated: 7/5/2026, 7:40:58 PM
class Solution:
  def concatenatedBinary(self, n: int) -> int:
    MOD = 1_000_000_007
    ans = 0

    def numberOfBits(n: int) -> int:
      return int(math.log2(n)) + 1

    for i in range(1, n + 1):
      ans = ((ans << numberOfBits(i)) + i) % MOD

    return ans