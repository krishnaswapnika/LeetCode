class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atmost(nums,k):
            if k <0:
                return 0
            n = len(nums)
            l=0
            ans=0
            temp=0
            for r in range(n):
                if nums[r] == 1:
                    temp+=1
                while temp > k:
                    if nums[l] == 1:
                        temp-=1
                    l+=1
                ans += r-l+1
            return ans
        ans = atmost(nums,goal)-atmost(nums,goal-1)
        return ans