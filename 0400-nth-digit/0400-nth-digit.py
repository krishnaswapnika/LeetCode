class Solution:
    def findNthDigit(self, n: int) -> int:
        digit = 1
        s = 1
        e = 9
        while n > digit*e:
            n -= digit * e
            digit += 1
            s *= 10
            e *= 10
        ans = s + (n-1) // digit 
        return int(str(ans)[(n-1)% digit])  