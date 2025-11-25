class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        d=-1
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                d = i
                break
        if d == -1:
            nums.reverse() 
            return nums
        for i in range(n-1,d,-1):
            if nums[i] >nums[d]:
                nums[i], nums[d] = nums[d], nums[i]
                break
        nums[d+1:]=reversed(nums[d+1:])
