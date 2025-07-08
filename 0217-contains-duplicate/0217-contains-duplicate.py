class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]] += 1
            else:
                dic[nums[i]]  = 1
        for i in range(len(dic)):
            if dic[nums[i]] >= 2:
                return True
        return False
