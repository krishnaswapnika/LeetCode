class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]]=dic.get(nums[i],0)+1
        for k,v in dic.items():
            if dic[k]>=2:
                return True
        return False