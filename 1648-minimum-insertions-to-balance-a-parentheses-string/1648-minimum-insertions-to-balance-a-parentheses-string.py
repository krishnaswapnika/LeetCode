class Solution:
    def minInsertions(self, s: str) -> int:
        l = 0
        ans = 0 
        i = 0
        n = len(s)
        while i < n:
            if s[i] == "(":
                l += 1
                i += 1
            else:
                if i + 1 < n and s[i+1] == ")":
                    if l > 0:
                        l -= 1
                    else:
                        ans += 1
                    i += 2
                else:
                    if l > 0:
                        l -= 1
                        ans += 1
                    else:
                        ans += 2
                    i += 1
        ans += 2 * l
        return ans