class Solution:
    def possibleStringCount(self, word: str) -> int:
        a = []
        i = 0
        n = len(word)
        while i < n:
            j = i
            while j < n and word[j] == word[i]:
                j += 1
            a.append((word[i], j - i))
            i = j
        total = 1
        for idx, (char, count) in enumerate(a):
            if count > 1:
                total += count - 1
        return total
