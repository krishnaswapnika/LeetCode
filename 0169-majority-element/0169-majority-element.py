class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m= len(nums)//2
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]] += 1
            else:
                dic[nums[i]] = 1
        for key in dic:
            if dic[key] > m:
                return key

        


