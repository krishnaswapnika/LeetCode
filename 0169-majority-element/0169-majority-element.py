class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = 0
        num = None
        for i in nums:
            if c == 0:
                num = i
            c += (1 if i==num else -1)
        return num

        


