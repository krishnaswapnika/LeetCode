class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        x = n - 2
        while x>=0:
            if nums[x] < nums[x+1]:
                break
            x -= 1
        if x<0:
            nums.reverse()
        else:
            l = n-1
            while l>x:
                if nums[x] < nums[l]:
                    break
                l-=1
            nums[x],nums[l] = nums[l], nums[x]
            nums[x+1:] = nums[x+1:][::-1]
        return nums
