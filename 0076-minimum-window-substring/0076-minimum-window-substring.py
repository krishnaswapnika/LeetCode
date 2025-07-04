class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map = Counter(t)
        win = defaultdict(int)
        have, need = 0, len(t_map)
        res, res_len = [-1, -1], float("inf")
        l = 0
        for r in range(len(s)):
            win[s[r]] += 1
            if s[r] in t_map and win[s[r]] == t_map[s[r]]:
                have += 1
            while have == need:
                if (r-l+1) < res_len:
                    res = [l, r]
                    res_len = r-l+1
                win[s[l]] -= 1
                if s[l] in t_map and win[s[l]] < t_map[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""

