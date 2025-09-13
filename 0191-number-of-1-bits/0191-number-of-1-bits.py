class Solution:
    def hammingWeight(self, n: int) -> int:
        c = 0
        b = bin(n).replace("0b", "")
        for i in b:
            if i == "1":
                c += 1
        return c
