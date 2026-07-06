class Solution:
    def isPalindrome(self, s: str) -> bool:
        string="".join(filter(str.isalnum,s)).lower()
        if string==string[::-1]:
            return True
        else:
            return False