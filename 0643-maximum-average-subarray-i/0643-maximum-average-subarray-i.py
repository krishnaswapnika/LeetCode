class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        tem = sum(nums[:k])
        maxs =tem
        for i in range(k, len(nums)):
            tem += nums[i]- nums[i - k]
            maxs= max(maxs, tem)
        return maxs/k
