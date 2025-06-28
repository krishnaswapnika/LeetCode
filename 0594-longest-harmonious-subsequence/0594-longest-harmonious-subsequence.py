class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        l =0
        ans =0
        for r in range(len(nums)):
            while nums[r]- nums[l] > 1:
                l+=1
            if nums[r]- nums[l] == 1:
                ans = max(ans, r-l+1)
        return ans



