class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        max_count = 0
        l= 0
        res= 0
        for r in range(len(s)):
            index = ord(s[r]) - ord('A')
            count[index] += 1
            max_count = max(max_count, count[index])
            if (r-l+1) - max_count > k:
                count[ord(s[l]) - ord('A')] -= 1
                l += 1
            res = max(res, r-l+ 1)
        return res

