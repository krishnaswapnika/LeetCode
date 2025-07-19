class Solution:
    def isPalindrome(self, s: str) -> bool:
        f = ''.join(char.lower() for char in s if char.isalnum())
        return f == f[::-1]

