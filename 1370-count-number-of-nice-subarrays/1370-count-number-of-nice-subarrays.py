class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atmostk(arr,k):
            l=0
            n=len(arr)
            ans = 0
            temp = 0
            for r in range(n):
                if arr[r] %2==1:
                    temp += 1
                while temp >k:
                    if arr[l] %2 ==1:
                        temp -= 1
                    l+=1
                ans += r-l+1
            return ans
        return atmostk(nums,k) - atmostk(nums,k-1)