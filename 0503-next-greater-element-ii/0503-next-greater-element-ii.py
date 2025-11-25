class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res = [-1]*n
        s=[]
        for i in range(2):
            for j in range(n-1,-1,-1):
                while s and s[-1] <= nums[j]:
                    s.pop()
                if s:res[j]=s[-1]
                s.append(nums[j])
        return res
