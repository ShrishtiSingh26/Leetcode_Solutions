# Last updated: 7/6/2026, 11:08:47 AM
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        string="".join(filter(str.isalnum,s)).lower()
4        if string==string[::-1]:
5            return True
6        else:
7            return False