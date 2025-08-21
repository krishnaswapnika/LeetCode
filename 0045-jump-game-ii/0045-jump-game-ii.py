class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n<=1:
            return 0
        j = 0
        f =0
        c=0
        for i in range(n-1):
            f = max(f, i+nums[i])
            if i==c:
                j+=1
                c=f
                if c>n-1:
                    break
        return j
