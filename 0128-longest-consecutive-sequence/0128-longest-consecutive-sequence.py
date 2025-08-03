class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        long = 1
        st = set(nums)
        for j in st:
            if j - 1 not in st:
                cnt = 1
                while j + 1 in st:
                    j += 1
                    cnt += 1
                long= max(long, cnt)
        return long