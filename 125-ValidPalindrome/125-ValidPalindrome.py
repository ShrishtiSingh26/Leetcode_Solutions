# Last updated: 7/5/2026, 7:42:06 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new="".join(filter(str.isalnum,s)).lower()
        if new==new[::-1]:
            return True
        else:
            return False