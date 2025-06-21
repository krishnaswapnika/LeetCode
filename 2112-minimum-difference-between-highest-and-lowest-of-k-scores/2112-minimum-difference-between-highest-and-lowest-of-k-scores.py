class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        l = 0
        nums.sort()
        ans = float("inf")
        n = len(nums)
        for r in range(n):
            if r-l ==k:
                l+=1
            if (r-l+1) == k:
                ans = min(ans, nums[r]-nums[l])
        return ans 


