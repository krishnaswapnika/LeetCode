class Solution:
    def reverseWords(self, s: str) -> str:
        w = s.strip().split()
        rw = w[::-1]
        return ' '.join(rw)