class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        w = set()
        for i in range(len(nums)):
            if nums[i] in w:
                return True
            w.add(nums[i])
            if len(w) > k:
                w.remove(nums[i - k])
        return False
