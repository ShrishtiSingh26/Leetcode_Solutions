# Last updated: 7/6/2026, 10:28:05 AM
1class Solution:
2    def findNumbers(self, nums: List[int]) -> int:
3        count=0
4        for i in nums:
5            l=len(str(abs(i)))
6            if l%2==0:
7                count+=1
8        return count