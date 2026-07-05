# Last updated: 7/5/2026, 7:53:07 PM
1class Solution:
2  def twoSum(self, nums: list[int], target: int) -> list[int]:
3    numToIndex = {}
4
5    for i, num in enumerate(nums):
6      if target - num in numToIndex:
7        return numToIndex[target - num], i
8      numToIndex[num] = i