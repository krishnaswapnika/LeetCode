class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n= len(nums1)
        m = len(nums2)
        ans = 0
        dp = [[0] *(m+1)  for _ in range(n+1)]
        for i in range(n-1, -1,-1):
            for j in range(m-1, -1, -1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                    ans = max(ans, dp[i][j])
        return ans 
